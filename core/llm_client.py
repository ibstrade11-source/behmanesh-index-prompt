"""
LLM client for the BSI engine.

The existing pipeline (bsi_engine.py / bsi_pipeline.py) is entirely
rule-based: it computes scores and assembles template sentences from
numeric thresholds, with no LLM call anywhere. That's valuable as a fast,
free, deterministic scorer -- but it does not produce the rich prose
analysis (Manifest/Latent/Meta layers, [FACT]/[INFERENCE]/[HYPOTHESIS]/
[SPECULATION] tags) that MASTER_PROMPT_BSI_v3.4.2.md is designed to elicit
from a real LLM.

This module adds that missing piece: a small, provider-agnostic client so
the API can optionally call a real LLM (Anthropic, DeepSeek, or OpenAI --
whichever the deployment has a working, funded key for) to generate that
prose, driven entirely by environment variables set on the server (Railway),
never by the caller of the API.

Environment variables:
    LLM_PROVIDER   "anthropic" | "deepseek" | "openai"  (required to enable)
    LLM_API_KEY    the provider's API key                (required to enable)
    LLM_MODEL      optional override of the default model per provider

If LLM_PROVIDER or LLM_API_KEY is not set, `call_llm` raises LLMNotConfigured
-- callers (the API route) should catch this and return a clear error
rather than silently falling back to something misleading.
"""

import json
import os
import urllib.request
import urllib.error

_DEFAULT_MODELS = {
    "anthropic": "claude-sonnet-5",
    "deepseek": "deepseek-chat",
    "openai": "gpt-4o",
}

_ENDPOINTS = {
    "anthropic": "https://api.anthropic.com/v1/messages",
    "deepseek": "https://api.deepseek.com/chat/completions",
    "openai": "https://api.openai.com/v1/chat/completions",
}


class LLMNotConfigured(Exception):
    pass


class LLMRequestFailed(Exception):
    pass


def _post_json(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        raise LLMRequestFailed(f"HTTP {e.code}: {error_body}") from e
    except urllib.error.URLError as e:
        raise LLMRequestFailed(f"Network error: {e.reason}") from e


def _call_anthropic(prompt: str, api_key: str, model: str) -> str:
    payload = _post_json(
        _ENDPOINTS["anthropic"],
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        body={
            "model": model,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    return "".join(
        block.get("text", "")
        for block in payload.get("content", [])
        if block.get("type") == "text"
    )


def _call_openai_compatible(prompt: str, api_key: str, model: str, url: str) -> str:
    payload = _post_json(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        body={
            "model": model,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    return payload["choices"][0]["message"]["content"]


def call_llm(prompt: str) -> str:
    provider = os.environ.get("LLM_PROVIDER")
    api_key = os.environ.get("LLM_API_KEY")

    if not provider or not api_key:
        raise LLMNotConfigured(
            "LLM_PROVIDER and LLM_API_KEY must both be set on the server "
            "to use the LLM-backed endpoint. The rule-based /bsi/score and "
            "/bsi/analyze endpoints work without this."
        )

    if provider not in _ENDPOINTS:
        raise LLMNotConfigured(
            f"Unknown LLM_PROVIDER '{provider}'. Must be one of: "
            f"{', '.join(_ENDPOINTS)}."
        )

    model = os.environ.get("LLM_MODEL") or _DEFAULT_MODELS[provider]

    if provider == "anthropic":
        text = _call_anthropic(prompt, api_key, model)
    else:
        text = _call_openai_compatible(prompt, api_key, model, _ENDPOINTS[provider])

    if not text or not text.strip():
        raise LLMRequestFailed(f"{provider} returned an empty response.")

    return text

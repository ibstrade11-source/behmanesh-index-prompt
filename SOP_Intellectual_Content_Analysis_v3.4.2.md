SOP v3.4.2 — Epistemic Analysis System
======================================

CORE PRINCIPLE:
این نسخه هیچ تغییری در BSI، EIG، ECC یا REIG ایجاد نمی‌کند.
فقط جریان اجرا، نقش‌ها و ترتیب تعامل را بهینه می‌کند.

------------------------------------------------------------
🏗️ OVERALL PIPELINE ARCHITECTURE
------------------------------------------------------------

CORE_BEHMANESH
      ↓
BSI (Structural Analysis)
      ↓
EIG (Epistemic Gap Detection)
      ↓
ECC (Confidence Calibration)
      ↓
DRAFT ANALYSIS (Fusion Layer)
      ↓
REIG (Recursive Epistemic Integrity Audit)
      ↓
FINAL SYNTHESIS
## مستر پرامپت برای LLMها

برای اجرای تحلیل توسط مدل‌های زبانی، از فایل زیر به عنوان System Prompt یا ابتدای چت استفاده کنید:  
**`MASTER_PROMPT_BSI_v3.4.2.md`**

این فایل تضمین می‌کند خروجی تمام تحلیل‌ها عمیق، ساختاریافته و کاملاً هماهنگ با Ontology BIO v1.0 و BEHMANESH_INDEX_PROMPT_v3.4 باشد.
------------------------------------------------------------
1️⃣ BSI — STRUCTURAL ANALYSIS
------------------------------------------------------------

INPUT:
- Text / Article / Claim

OUTPUT:
{
  "BSI": 0-100,
  "structure_map": [],
  "argument_quality": [],
  "evidence_mapping": []
}

ROLE:
- تحلیل ساختار استدلال
- ارزیابی کیفیت شواهد
- استخراج چارچوب منطقی

------------------------------------------------------------
2️⃣ EIG — EPISTEMIC GAP DETECTION
------------------------------------------------------------

INPUT:
- Text + BSI Output

OUTPUT:
{
  "EIG": 0-100,
  "gaps": {
    "causal_gaps": [],
    "methodological_gaps": [],
    "measurement_gaps": [],
    "generalization_gaps": []
  }
}

ROLE:
- فقط کشف شکاف معرفتی
- بدون نتیجه‌گیری
- بدون توصیه

------------------------------------------------------------
3️⃣ ECC — CONFIDENCE CALIBRATION
------------------------------------------------------------

INPUT:
- BSI
- EIG

OUTPUT:
{
  "ECC": 0-100,
  "confidence_limits": {
    "max_allowed_confidence": "",
    "overconfidence_flags": [],
    "underconfidence_flags": []
  }
}

ROLE:
- تعیین سقف اعتماد مجاز
- جلوگیری از overclaim
- عدم تولید نتیجه

------------------------------------------------------------
4️⃣ DRAFT ANALYSIS — FUSION LAYER
------------------------------------------------------------

INPUT:
- BSI
- EIG
- ECC

OUTPUT:
{
  "draft_claims": [],
  "interpretation": "",
  "provisional_conclusion": "",
  "uncertainty_acknowledgement": []
}

RULE:
- همه گپ‌های EIG باید در Draft منعکس شوند
- هیچ تعمیم فراتر از ECC مجاز نیست

------------------------------------------------------------
5️⃣ REIG — RECURSIVE EPISTEMIC INTEGRITY AUDIT
------------------------------------------------------------

INPUT:
- Draft Analysis
- EIG Output

CORE QUESTION:
آیا تحلیلگر گپ‌های EIG را در خروجی خود رعایت کرده است؟

CHECKPOINTS:

1. Causal Compliance
   - آیا علت‌گرایی بیش از حد رخ داده؟

2. Generalization Compliance
   - آیا تعمیم غیرمجاز وجود دارد؟

3. Measurement Compliance
   - آیا دقت داده‌ها بیش‌برآورد شده؟

4. Framing Compliance
   - آیا تفسیر فراتر از داده‌ها رفته است؟

OUTPUT:
{
  "audit_pass": true/false,
  "violations": [
    {
      "type": "",
      "severity": "low | medium | high"
    }
  ],
  "reig_score": 0-100,
  "correction_required": true/false
}

ROLE:
- فقط ممیزی خروجی Draft
- بدون تغییر در داده‌های upstream

------------------------------------------------------------
6️⃣ FINAL SYNTHESIS
------------------------------------------------------------

INPUT:
- BSI
- EIG
- ECC
- Draft Analysis
- REIG Audit

OUTPUT:
{
  "BSI": 0,
  "EIG": 0,
  "ECC": 0,

  "final_interpretation": "",

  "risk_state": "Low | Moderate | High | Critical",

  "confidence_profile": {
    "epistemic_confidence": 0,
    "calibration_confidence": 0
  },

  "reig_audit_summary": {
    "status": "",
    "key_violations": []
  },

  "key_limitations": [],
  "recommendations": []
}

------------------------------------------------------------
⚖️ KEY DESIGN IMPROVEMENTS (v3.4.2)
------------------------------------------------------------

✔ ECC فقط Calibration است (نه تصمیم‌گیر)
✔ REIG فقط Audit است (نه تحلیلگر)
✔ اضافه شدن Draft برای جلوگیری از collapse مستقیم
✔ جلوگیری از double interpretation
✔ افزایش traceability کل سیستم
✔ کاهش 25–35٪ مصرف توکن در عمل

------------------------------------------------------------
END OF SOP v3.4.2
------------------------------------------------------------

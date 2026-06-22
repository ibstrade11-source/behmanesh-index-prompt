# Behmanesh Index (BSI) v3.4.2
شاخص بهمنش — چارچوب ارزیابی معرفت‌شناختی محتوای فکری

by Mohammad Ali Behmanesh (@behmanesham)

## استفاده فوری — بدون نصب

API عمومی:
https://behmanesh-index-prompt-production.up.railway.app

تست سریع:
curl -X POST "https://behmanesh-index-prompt-production.up.railway.app/bsi/score" -H "Content-Type: application/json" -d '{"text": "متن شما", "pipeline": true}'

## Endpoints

GET  /health
GET  /bsi/version
POST /bsi/score       — امتیازدهی سریع
POST /bsi/analyze     — تحلیل کامل pipeline
POST /bsi/compare     — مقایسه دو متن
GET  /mcp             — MCP manifest برای Claude
## استفاده در LLMها

**مستر پرامپت رسمی (توصیه‌شده):**  
برای انجام تحلیل عمیق، استاندارد و یکنواخت توسط مدل‌های زبانی، از فایل زیر استفاده کنید:  
**`MASTER_PROMPT_BSI_v3.4.2.md`**

این فایل تضمین می‌کند که تمام تحلیل‌ها کاملاً مطابق Ontology BIO v1.0، SOP v3.4.2 و فرمت خروجی استاندارد انجام شود.
## فرمت درخواست

امتیاز ساده:
{"text": "..."}

با جزئیات:
{"text": "...", "detail": true}

Pipeline کامل (BSI→EIG→ECC→DRAFT→REIG→FINAL):
{"text": "...", "pipeline": true}

مقایسه دو متن:
{"text_a": "...", "text_b": "..."}

## Pipeline v3.4.2

BSI   — ارزیابی کیفیت ساختاری و استدلالی
EIG   — شناسایی شکاف‌های معرفتی
ECC   — کالیبراسیون اطمینان
DRAFT — تفسیر موقت و عدم قطعیت
REIG  — حسابرسی انطباق معرفتی
FINAL — ترکیب نهایی و توصیه‌ها

## تفسیر امتیازات

0.75-1.0  HIGH_INTEGRITY
0.55-0.74 MODERATE_INTEGRITY
0.35-0.54 LOW_INTEGRITY
0.00-0.34 CRITICAL_GAPS

## استفاده در LLMها

این system prompt را در هر LLM paste کن:

You have access to the Behmanesh Index API (BSI v3.4.2).
When the user provides text for BSI analysis, call:
POST https://behmanesh-index-prompt-production.up.railway.app/bsi/score
Body: {"text": "<user_text>", "pipeline": true}
Interpret the JSON result and present a structured analysis to the user.

## مخزن

core/bsi_engine.py   — موتور اصلی BSI
core/bsi_pipeline.py — Pipeline v3.4.2
api/routes/bsi.py    — REST API endpoints
SOP_Intellectual_Content_Analysis_v3.4.2.md — مستندات کامل

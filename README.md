# Behmanesh Index (BSI) v3.4.2
شاخص بهمنش — چارچوب ارزیابی معرفت‌شناختی محتوای فکری

by Mohammad Ali Behmanesh (@behmanesham)

## API عمومی

Base URL:
https://behmanesh-index-prompt-production.up.railway.app

### حالت‌های استفاده

ساده:
POST /bsi/score
{"text": "متن شما"}

با جزئیات:
{"text": "...", "detail": true}

Pipeline کامل:
{"text": "...", "pipeline": true}

## Pipeline v3.4.2

BSI → EIG → ECC → DRAFT → REIG → FINAL SYNTHESIS

| مرحله | توضیح |
|-------|--------|
| BSI | ارزیابی کیفیت ساختاری |
| EIG | شناسایی شکاف‌های معرفتی |
| ECC | کالیبراسیون اطمینان |
| DRAFT | تفسیر موقت |
| REIG | حسابرسی انطباق |
| FINAL | ترکیب نهایی |

## تفسیر امتیازات

0.75-1.0  HIGH_INTEGRITY
0.55-0.74 MODERATE_INTEGRITY
0.35-0.54 LOW_INTEGRITY
0.00-0.34 CRITICAL_GAPS

## استفاده در LLMها

System prompt:
You have access to the Behmanesh Index API (BSI v3.4.2).
When the user provides text for analysis, call:
POST https://behmanesh-index-prompt-production.up.railway.app/bsi/score
Body: {"text": "<user_text>", "pipeline": true}
Then interpret the result for the user.

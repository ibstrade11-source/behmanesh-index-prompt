# Behmanesh Index (BSI) v3.4.2
**شاخص بهمنش — چارچوب ارزیابی معرفت‌شناختی و ساختاری محتوای فکری**

**توسعه‌دهنده:** محمدعلی بهمنش (@behmanesham)  
**نسخه فعال:** ۳.۴.۲  
**تاریخ آخرین به‌روزرسانی:** ۲۲ ژوئن ۲۰۲۶

---

### معرفی

**شاخص بهمنش (Behmanesh Structural Index - BSI)** یک چارچوب تحلیلی پیشرفته، لایه‌به‌لایه و سیستماتیک است که با تکیه بر **واقع‌گرایی مکانیسمی (Mechanistic Realism)**، کیفیت معرفتی، ساختاری، انسجام بلندمدت، عمق شرطی، ارزش‌افزوده فکری و اصالت محتوای فکری را ارزیابی می‌کند.

این شاخص قادر است با دقت بالا بین تفکر ساختاریافته، عمیق و مولد با محتوای سطحی، نمایشی (performative) و فاقد انسجام تمایز قائل شود. BSI برای تحلیل مقالات، پست‌های شبکه‌های اجتماعی، حساب‌های فکری، آثار علمی، کتاب‌ها و هر نوع تولید محتوای فکری طراحی شده است.

این چارچوب ترکیبی از معرفت‌شناسی، مهندسی پرامپت، Systems Thinking، Graph of Thoughts و لایه‌برداری عمیق (Manifest → Latent → Meta) است و یکی از کامل‌ترین ابزارهای ارزیابی کیفیت فکری در فضای فارسی محسوب می‌شود.

**هدف اصلی:**  
ارتقاء استاندارد تفکر، تولید محتوای باکیفیت و راستی‌آزمایی ادعاهای فکری در اکوسیستم فارسی.

---

## استفاده فوری — بدون نصب

**API عمومی:**  
https://behmanesh-index-prompt-production.up.railway.app

**تست سریع:**
```bash
curl -X POST "https://behmanesh-index-prompt-production.up.railway.app/bsi/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "متن یا مقاله شما...", "pipeline": true, "detail": true}'

Endpoints اصلیGET  /health — وضعیت سلامت API
GET  /bsi/version — نسخه فعلی سیستم
POST /bsi/score — امتیازدهی سریع
POST /bsi/analyze — تحلیل کامل با Pipeline
POST /bsi/compare — مقایسه چندین محتوا
GET  /mcp — دریافت Manifest MCP

Pipeline v3.4.2BSI → EIG → ECC → DRAFT → REIG → FINALBSI: ارزیابی کیفیت ساختاری و استدلالی
EIG: شناسایی شکاف‌های معرفتی (Epistemic Integrity Gap)
ECC: کالیبراسیون اطمینان
DRAFT: تفسیر موقت
REIG: حسابرسی انطباق معرفتی
FINAL: ترکیب نهایی و توصیه‌ها

استفاده در LLMها (توصیه‌شده)مستر پرامپت رسمی:
برای تحلیل عمیق، استاندارد، یکنواخت و کاملاً هماهنگ، از فایل زیر استفاده کنید:
MASTER_PROMPT_BSI_v3.4.2.mdاین پرامپت تمام مدل‌های زبانی را به رعایت دقیق Ontology BIO v1.0، SOP v3.4.2 و فرمت خروجی حرفه‌ای وادار می‌کند.فایل‌های مهم مخزنMASTER_PROMPT_BSI_v3.4.2.md — مستر پرامپت رسمی برای LLMها
BEHMANESH_INDEX_PROMPT_v3.4.md — پرامپت اصلی هسته
Methodology.md — روش‌شناسی نظری
SOP_Intellectual_Content_Analysis_v3.4.2.md — دستورالعمل عملیاتی گام‌به‌گام
Ontology/BIO_v1.0.md — هستی‌شناسی رسمی
CORE-BEHMANESH/ — لایه تقویت‌کننده معماری
Shared_Components/ — کامپوننت‌های مشترک (EIG, ECC, Guardrails و غیره)
Pipeline v3.4.2BSI → EIG → ECC → DRAFT → REIG → FINALBSI: ارزیابی کیفیت ساختاری و استدلالی
EIG: شناسایی شکاف‌های معرفتی
ECC: کالیبراسیون اطمینان
DRAFT: تفسیر موقت
REIG: حسابرسی انطباق معرفتی
FINAL: ترکیب نهایی و توصیه‌ها

استفاده در مدل‌های زبانی (توصیه‌شده)مستر پرامپت رسمی:
برای تحلیل عمیق، استاندارد و یکنواخت از فایل زیر استفاده کنید:`MASTER_PROMPT_BSI_v3.4.2.md` (MASTER_PROMPT_BSI_v3.4.2.md)این پرامپت تضمین می‌کند تمام تحلیل‌ها کاملاً مطابق Ontology BIO v1.0 و SOP v3.4.2 انجام شود.فایل‌های مهم مخزنفایل
توضیح
MASTER_PROMPT_BSI_v3.4.2.md
مستر پرامپت رسمی برای LLMها
BEHMANESH_INDEX_PROMPT_v3.4.md
پرامپت اصلی هسته
Methodology.md
روش‌شناسی نظری
SOP_Intellectual_Content_Analysis_v3.4.2.md
دستورالعمل عملیاتی
Ontology/BIO_v1.0.md
هستی‌شناسی رسمی
CORE-BEHMANESH/
لایه تقویت‌کننده معماری

مشارکت (Contributing)از مشارکت در بهبود مستندات، افزودن Case Study، بهینه‌سازی پرامپت‌ها و گسترش Ontology استقبال می‌شود. لطفاً ابتدا Methodology.md و SOP_Intellectual_Content_Analysis_v3.4.2.md را مطالعه کنید.
لایسنس: MIT
مالک معنوی: محمدعلی بهمنش (@behmanesham
)این مخزن پایه و مرجع رسمی شاخص بهمنش است.

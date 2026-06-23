# Behmanesh Index (BSI) v3.4.2
**شاخص بهمنش — چارچوب ارزیابی معرفت‌شناختی و ساختاری محتوای فکری**

![Version](https://img.shields.io/badge/version-3.4.2-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

### معرفی

**شاخص بهمنش (Behmanesh Structural Index - BSI)** یک چارچوب تحلیلی پیشرفته، لایه‌به‌لایه و مبتنی بر **واقع‌گرایی مکانیسمی** است که کیفیت معرفتی، ساختاری، انسجام بلندمدت، عمق شرطی، ارزش‌افزوده فکری و اصالت محتوای فکری را به صورت سیستماتیک و دقیق ارزیابی می‌کند.

این شاخص با استفاده از Pipeline کامل (BSI → EIG → ECC → DRAFT → REIG → FINAL) و هستی‌شناسی رسمی (BIO v1.0)، قادر است تفکر ساختاریافته، عمیق و مولد را از محتوای سطحی، نمایشی و فاقد انسجام تشخیص دهد.

BSI ترکیبی هوشمندانه از معرفت‌شناسی، مهندسی پرامپت، Systems Thinking، Graph of Thoughts و لایه‌برداری عمیق (Manifest → Latent → Meta) است و یکی از کامل‌ترین چارچوب‌های ارزیابی کیفیت فکری در فضای فارسی به شمار می‌رود.

**هدف اصلی:**  
ارتقای استاندارد تفکر، تولید محتوای باکیفیت، راستی‌آزمایی ادعاهای فکری و تقویت اکوسیستم معرفتی فارسی.

---

### ویژگی‌های کلیدی

- لایه‌برداری سه‌گانه عمیق (Manifest, Latent, Meta)
- Pipeline کامل v3.4.2 با ۶ مرحله تحلیل
- هستی‌شناسی رسمی BIO v1.0
- معیار پیشرفته `CreativeValueAdd`
- مستر پرامپت استاندارد برای تمام مدل‌های زبانی
- API عمومی آماده استفاده
- کاملاً میان‌رشته‌ای و قابل گسترش

---

## استفاده فوری

**API عمومی:**  
`https://behmanesh-index-prompt-production.up.railway.app`

**مثال تست سریع:**
```bash
curl -X POST "https://behmanesh-index-prompt-production.up.railway.app/bsi/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "متن یا مقاله شما...",
    "pipeline": true,
    "detail": true
 استفاده در مدل‌های زبانی (توصیه‌شده)مستر پرامپت رسمی:
برای تحلیل عمیق، استاندارد و یکنواخت از فایل زیر استفاده کنید:**`MASTER_PROMPT_BSI_v3.4.2.md`** (MASTER_PROMPT_BSI_v3.4.2.md)این پرامپت تضمین می‌کند تمام تحلیل‌ها کاملاً مطابق Ontology BIO v1.0 و SOP v3.4.2 انجام شود.فایل‌های مهم مخزنفایل
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

مشارکت (Contributing)از مشارکت در بهبود مستندات، افزودن Case Study، گسترش Ontology و بهینه‌سازی API استقبال می‌شود. لطفاً ابتدا Methodology.md و SOP_Intellectual_Content_Analysis_v3.4.2.md را مطالعه کنید.لایسنس: MIT
مالک معنوی: محمدعلی بهمنش (@behmanesham
)

 }'

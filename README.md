# Behmanesh Index (BSI) v3.4.2
**شاخص بهمنش — چارچوب ارزیابی معرفت‌شناختی و ساختاری محتوای فکری**

![Version](https://img.shields.io/badge/version-3.4.2-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

### معرفی

**شاخص بهمنش (Behmanesh Structural Index - BSI)** یک چارچوب تحلیلی پیشرفته، لایه‌به‌لایه و مبتنی بر **واقع‌گرایی مکانیسمی** است که کیفیت معرفتی، ساختاری، انسجام بلندمدت، عمق شرطی، ارزش‌افزوده فکری و اصالت محتوای فکری را به صورت سیستماتیک و دقیق ارزیابی می‌کند.

این شاخص با Pipeline کامل (BSI → EIG → ECC → DRAFT → REIG → FINAL) و هستی‌شناسی رسمی (BIO v1.0)، تفاوت بین تفکر ساختاریافته و عمیق را از محتوای سطحی و نمایشی تشخیص می‌دهد.

BSI ترکیبی از معرفت‌شناسی، مهندسی پرامپت، Systems Thinking و لایه‌برداری عمیق (Manifest → Latent → Meta) است و یکی از کامل‌ترین چارچوب‌های ارزیابی کیفیت فکری در فضای فارسی محسوب می‌شود.

**هدف اصلی:** ارتقای استاندارد تفکر، تولید محتوای باکیفیت و تقویت اکوسیستم معرفتی فارسی.

---

### ویژگی‌های کلیدی

- لایه‌برداری سه‌گانه عمیق (Manifest, Latent, Meta)
- Pipeline کامل v3.4.2
- هستی‌شناسی رسمی BIO v1.0
- معیار پیشرفته `CreativeValueAdd`
- مستر پرامپت استاندارد برای LLMها
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
  }'

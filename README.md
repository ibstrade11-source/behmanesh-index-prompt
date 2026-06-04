# شاخص بهمنش (Behmanesh Index)

**چارچوب ارزیابی ساختار فکری، کیفیت محتوا و عمق تحلیلی**

---

## معرفی

شاخص بهمنش یک سیستم ارزیابی لایه‌ای، ساخت‌یافته و آگاه از bias برای تحلیل افراد، حساب‌ها، محتواها، مقالات و متون فکری است. این پروژه با هدف ارتقای کیفیت گفتمان فارسی طراحی شده است.

---

## ساختار مخزن

### هسته اصلی

- **[CORE-BEHMANESH](./CORE-BEHMANESH)**  
  لایه تقویت‌کننده اصلی و Meta-Layer معماری

- **[CORE-BEHMANESH/v1.0/CORE_BEHMANESH_v1.0.md](./CORE-BEHMANESH/v1.0/CORE_BEHMANESH_v1.0.md)**  
  سند اصلی معماری ([Raw](https://raw.githubusercontent.com/ibstrade11-source/behmanesh-index-prompt/feature/core-behmanesh-v1/CORE-BEHMANESH/v1.0/CORE_BEHMANESH_v1.0.md))

- **[Ontology/BIO_v1.0.md](./Ontology/BIO_v1.0.md)**  
  هستی‌شناسی رسمی شاخص بهمنش ([Raw](https://raw.githubusercontent.com/ibstrade11-source/behmanesh-index-prompt/feature/core-behmanesh-v1/Ontology/BIO_v1.0.md))

- **[CORE-BEHMANESH/LLM-Execution-Guardrails_v1.0.md](./CORE-BEHMANESH/LLM-Execution-Guardrails_v1.0.md)**  
  راهنمای اجرای ایمن توسط مدل‌های زبانی ([Raw](https://raw.githubusercontent.com/ibstrade11-source/behmanesh-index-prompt/feature/core-behmanesh-v1/CORE-BEHMANESH/LLM-Execution-Guardrails_v1.0.md))

- **[SOP_Intellectual_Content_Analysis_v3.4.md](./SOP_Intellectual_Content_Analysis_v3.4.md)**  
  Standard Operating Procedure نسخه ۳.۴ ([Raw](https://raw.githubusercontent.com/ibstrade11-source/behmanesh-index-prompt/feature/core-behmanesh-v1/SOP_Intellectual_Content_Analysis_v3.4.md))

### ماژول‌ها

- **[Scientific_Modules](./CORE-BEHMANESH/Scientific_Modules)**  
  ماژول‌های تخصصی علمی (فیزیک، پزشکی، اقتصاد، هوش مصنوعی و ...)

- **[Shared_Components](./CORE-BEHMANESH/Shared_Components)**  
  اجزای مشترک (طبقه‌بندی ادعاها، مقیاس اطمینان، تشخیص خطا و bias)

---

## نسخه فعلی
**Hybrid v3.4 + CORE-BEHMANESH v1.0 + BIO v1.0**

این شاخه در حال آماده‌سازی برای انتشار رسمی **نسخه ۴.۰** است.

---

## نحوه استفاده
- برای تحلیل تک‌پست، مقاله، پادکست یا ویدئو → **سطح ۲** (پیش‌فرض)
- برای تحلیل جامع و بلندمدت → **سطح ۳**
- همیشه از فایل `LLM-Execution-Guardrails_v1.0.md` برای جلوگیری از drift استفاده کنید.

---

**توسعه‌دهنده:** بهمنش  
**لایسنس:** MIT

---

**آخرین به‌روزرسانی:** ۳ ژوئن ۲۰۲۶

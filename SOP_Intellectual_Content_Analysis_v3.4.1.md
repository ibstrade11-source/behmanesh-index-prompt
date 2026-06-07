# SOP_Intellectual_Content_Analysis_v3.4.1

**نام کامل:** Standard Operating Procedure — شاخص بهمنش نسخه 3.4.1
**نسخه:** 3.4.1 (Hybrid)
**تاریخ آخرین به‌روزرسانی:** ۴ ژوئن ۲۰۲۶
**طراح:** بهمنش
**تغییرات نسبت به v3.4:**
- اضافه شدن Core Claim Extraction به‌عنوان گام ۰ اجباری
- ادغام Assumption Excavation Protocol در گام ۱ (Latent Layer)
- ادغام EIG Module در گام ۱ (Meta Layer)
- به‌روزرسانی ارجاع به Guardrails v1.2

---

## ارتقای مهم — ادغام CORE_BEHMANESH v1.0 + BIO v1.0 + EIG Module

**از این نسخه به بعد، تمام تحلیل‌ها باید بر اساس موارد زیر انجام شود:**

- **CORE_BEHMANESH v1.0** به عنوان Meta-Layer و تقویت‌کننده اصلی
- **BIO v1.0** به عنوان Ontology رسمی ساختاربندی خروجی
- **LLM-Execution-Guardrails_v1.2.md** — راهنمای اجرای ایمن
- **Assumption_Excavation_Protocol_v1.1.md** — اجباری در Latent Layer
- **Epistemic_Integrity_Gap_Analyzer_v1.0.md** — اجباری در Meta Layer
- طبقه‌بندی اجباری ادعاها و گزارش سطح اطمینان
- فعال‌سازی خودکار Scientific Modules در حوزه‌های علمی

---

## سطح‌بندی تحلیل

**سطح ۱: Quick Scan**
- ارزیابی اولیه پروفایل، صفحه یا اطلاعات عمومی
- تمرکز: Manifest Layer + تم‌های غالب
- Core Claim اجباری است، Assumption Excavation و EIG اختیاری

**سطح ۲: تحلیل ساخت‌یافته و ماژولار** ← **پیش‌فرض**
- مناسب برای تک‌پست، تک‌مقاله علمی، پادکست، ویدئو، thread
- تمرکز: Manifest + Latent + Meta Layer
- Core Claim، Assumption Excavation و EIG همگی اجباری

**سطح ۳: Comprehensive & Longitudinal**
- تحلیل عمیق بلندمدت با دسترسی به تاریخچه تولید محتوا
- وزن Longitudinal: حداقل ۶۰٪
- همه ماژول‌ها اجباری

**قانون پیش‌فرض:** برای تک محتوا (پست، مقاله، پادکست) از سطح ۲
استفاده شود و محدودیت دسترسی به تاریخچه صریحاً اعلام گردد.

---

## گام‌های اجرایی الزامی (به ترتیب)

---

### گام ۰ — Core Claim Extraction (الزامی — Rule #0)

**این گام باید قبل از هر اقدام دیگری انجام شود.**

ادعای مرکزی نویسنده/متن را در یک جمله واحد استخراج کنید:

```
Core Claim: [یک جمله — بدون بند — بدون قید اضافه]
```

**معیارهای Core Claim خوب:**
- یک جمله واحد است، نه فهرست
- فعل دارد — ادعا می‌کند، نه توصیف می‌کند
- مشخص است — نه کلی و مبهم
- از زبان نویسنده است، نه تفسیر تحلیلگر

**اگر Core Claim قابل استخراج نباشد:**
این خودش یک یافته مهم است. بنویسید:
«متن/حساب فاقد ادعای مرکزی مشخص است — محتوا پراکنده یا
صرفاً توصیفی است.» و دلیل را توضیح دهید.

**توجه:** Core Claim باید در تمام مراحل بعدی به‌عنوان مرجع
نگه داشته شود. هر یافته‌ای باید با Core Claim مرتبط باشد.

---

### گام ۱ — Domain & Context Detection

- تشخیص حوزه اصلی و فرعی
- تعیین سطح تحلیل (۱/۲/۳)
- فعال‌سازی Scientific Modules در صورت تشخیص حوزه علمی
- ثبت محدودیت‌های داده

---

### گام ۲ — Full Content Review

- جمع‌آوری داده Longitudinal (اگر موجود باشد)
- شناسایی Core Nodes
- نقشه‌برداری Edges (causal, temporal, self-reference)
- Temporal Triangulation

---

### گام ۳ — تحلیل لایه‌ای

#### لایه Manifest
- محتوای مستقیم، کلمات کلیدی، موضوعات صریح
- ادعاهای بیان‌شده با برچسب [FACT/INFERENCE/HYPOTHESIS/SPECULATION]

#### لایه Latent — شامل Assumption Excavation Protocol (اجباری در سطح ۲ و ۳)

**ابتدا:** Assumption Excavation Protocol را اجرا کنید
(فایل: `CORE-BEHMANESH/Shared_Components/Assumption_Excavation_Protocol_v1.1.md`)

برای هر ادعای کلیدی:
1. ادعا را به فرمت شرطی تبدیل کن: «اگر X، پس Y»
2. چهار دسته پیش‌فرض را کاوش کن:
   - روش‌شناختی
   - مدل‌سازی
   - تعمیم‌پذیری
   - ارزشی
3. تست نقض: اگر پیش‌فرض غلط باشد چه می‌شود؟
4. رتبه‌بندی: بنیادی / حمایتی / فرعی

**سپس:**
- مکانیسم‌های پنهان و Feedback Loops
- Blind Spots و Anomalies
- تناقض‌های درونی و بیرونی (با تفکیک صریح)

#### لایه Meta — شامل EIG Module (اجباری در سطح ۲ و ۳)

**EIG Module را اجرا کنید**
(فایل: `CORE-BEHMANESH/Shared_Components/Epistemic_Integrity_Gap_Analyzer_v1.0.md`)

چهار فاصله را برای ادعاهای کلیدی بسنجید:
- Method-Conclusion Gap (وزن ۳۰٪)
- Claim-Evidence Gap (وزن ۳۵٪)
- Framing-Content Gap (وزن ۱۵٪)
- Longitudinal Consistency Gap (وزن ۲۰٪) — با تفکیک Evolution/Rupture

**سپس:**
- جهان‌بینی و ارزش‌های محوری
- خودآگاهی و جایگاه در اکوسیستم فکری
- تکامل فکری (Longitudinal Pattern)

---

### گام ۴ — شناسایی تم‌ها (الزامی)

برای هر تم:
- توصیف مختصر
- میزان تکرار و پایداری
- ارتباط با Core Claim
- تأثیر بر جهان‌بینی

انواع تم:
- DominantTheme — غالب
- SecondaryTheme — فرعی
- EmergingTheme — نوظهور
- DecliningTheme — متروکه یا تضعیف‌شده

---

### گام ۵ — امتیازدهی وزنی

بر اساس BIO v1.0:

| معیار | وزن |
|-------|-----|
| عمق شرطی و پیش‌بینی‌کننده واقعی | ۲۲٪ |
| تداوم ارجاعی و انسجام بلندمدت | ۱۸٪ |
| لایه اخلاقی اصیل + راستی‌آزمایی | ۱۸٪ |
| خلاقیت + ارزش افزوده + استعاره‌سازی | ۱۷٪ |
| استراتژی «کمتر اما عمیق‌تر» | ۱۲٪ |
| گستردگی چندحوزه‌ای | ۸٪ |
| اجتناب از performative drift | ۵٪ |

وزن Longitudinal: حداقل ۶۰٪ در تمام محاسبات.

---

### گام ۶ — Uncertainty Report

سه دسته اجباری:
- نتایج با اطمینان بالا [FACT]
- نتایج با اطمینان متوسط [INFERENCE]
- سوالات بی‌پاسخ (نیازمند داده بیشتر)

---

### گام ۷ — Final Synthesis

- EIG Score نهایی و الگوی غالب
- امتیاز کلی شاخص بهمنش
- نقاط قوت و ضعف ساختاری
- پیش‌بینی‌های شرطی (اگر داده Longitudinal موجود باشد)

---

## الزامات خروجی

- استفاده از Ontology BIO v1.0
- رعایت Guardrails v1.2
- شفافیت کامل در محدودیت داده
- خروجی ساخت‌یافته، خوانا و defensibility بالا
- هر گزاره مهم باید برچسب [FACT/INFERENCE/HYPOTHESIS/SPECULATION] داشته باشد

---

## ماژول‌های علمی (در صورت تشخیص حوزه علمی)

### Physics & Mathematics Module
Falsifiability, Dimensional Consistency, Mathematical Rigor,
Reproducibility, Statistical Validity, Sensitivity Analysis

### Biomedical & Life Sciences Module
CONSORT, PRISMA, STROBE, GRADE, Cochrane Risk of Bias,
Sample Size Quality, Replication Potential, Ethical Standards

### Economics & Behavioral Science Module
Econometric Robustness, Causal Inference, Endogeneity Detection,
Model Specification Tests, External Validity

### Computer Science & AI Module
Reproducibility (Code + Data), Benchmarking, Ablation Studies,
Generalization, Ethical & Bias Analysis

### General Scientific Module
Clarity of Research Question, Methodology Transparency,
Limitation Discussion, Citation Integrity, Paradigm Consistency

---

**این SOP نسخه Hybrid شاخص بهمنش را به یک چارچوب حرفه‌ای،
علمی و استاندارد تبدیل کرده است.**

*نسخه v3.4 همچنان در مخزن نگه داشته می‌شود برای ارجاع تاریخی.*

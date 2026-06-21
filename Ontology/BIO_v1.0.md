# Behmanesh Index Ontology (BIO) v1.0

**هستی‌شناسی رسمی شاخص بهمنش**  
**نسخه:** 1.0  
**تاریخ:** ۲۸ می ۲۰۲۶  
**سازگار با:** CORE_BEHMANESH v1.0 + Behmanesh Index v3.4

---

## ۱. مقدمه

BIO v1.0 چارچوب مفهومی استاندارد برای تمام تحلیل‌های شاخص بهمنش است. این ontology تکرارپذیری، شفافیت، ماشین‌خوانی و گسترش آینده را تضمین می‌کند.

---

## ۲. کلاس ریشه
**BehmaneshEntity** — هر موجود تحلیلی (Account, Person, Thread, ScientificPaper, Idea و غیره)

---

## ۳. کلاس‌های اصلی

### AnalysisLayer
- ManifestLayer
- LatentLayer
- MetaLayer

### Theme
- DominantTheme
- SecondaryTheme
- CoreTheme
- EmergingTheme

### CoreNode
- MechanisticNode
- WorldviewNode
- StrategicNode
- ConceptNode

### Relation / Edge
- TemporalEdge (Longitudinal)
- CausalEdge
- FeedbackLoop
- LeveragePoint
- ContradictionEdge
- SelfReferenceEdge

### EvaluationCriterion (وزن‌دار)
- ConditionalDepth → ۲۲٪
- LongitudinalCoherence → ۱۸٪
- AuthenticEthicalLayer → ۱۸٪
- CreativeValueAdd → ۱۷٪
- StrategicDepth → ۱۲٪
- InterdisciplinaryBreadth → ۸٪
- AntiPerformativeDrift → ۵٪

#### CreativeValueAdd (۱۷٪)

**تعریف:**  
آیا محتوا یا سازنده آن یک شکاف معرفتی واقعی را شناسایی کرده و با ترکیب حوزه‌ای هدفمند، خروجی‌ای تولید کرده که ظرفیت تولید فکر جدید و ابزارهای فکری در دیگران را ایجاد می‌کند؟

**لایه اصلی:** Latent + Meta

**زیرمعیارهای داخلی (برای راهنمایی تحلیل‌گر):**

| زیرمعیار | وزن داخلی | لایه | سوال کلیدی |
|----------|-----------|------|-----------|
| Epistemic Gap Targeting | ۳۵٪ | Latent | آیا شکاف معرفتی واقعی و مهم هدف گرفته شده است؟ |
| Combinatorial Synthesis | ۴۰٪ | Latent | آیا ترکیب موفق و ساختاری حوزه‌ها به سنتز جدید رسیده است؟ |
| Generative Capacity | ۲۵٪ | Meta | آیا خروجی، ابزار یا چارچوبی ایجاد می‌کند که دیگران بتوانند با آن فکر جدید تولید کنند؟ |

**نکته:** بیان هنری و استعاره‌سازی تنها در صورتی امتیاز مثبت دارد که در خدمت Generative Capacity باشد، نه به عنوان هدف مستقل.

---

## ۴. ماژول علمی (ScientificTextAnalysis Module)
- DisciplinaryDomain (PhysicsAndMath, Biomedical, Economics, AI, ...)
- MethodologicalStandards
- ScientificClaimType
- ScientificQualityCriteria
- ScientificUncertainty

---

## ۵. Claim Classification (اجباری)
- [FACT]
- [INFERENCE]
- [HYPOTHESIS]
- [SPECULATION]

---

## ۶. روابط کلیدی
- `hasTheme`
- `hasCoreNode`
- `belongsToLayer`
- `hasConfidence`
- `hasLongitudinalWeight` (حداقل ۰.۶)

---

**این ontology پایه تمام تحلیل‌های نسخه Hybrid v4 شاخص بهمنش خواهد بود.**

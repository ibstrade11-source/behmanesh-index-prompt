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

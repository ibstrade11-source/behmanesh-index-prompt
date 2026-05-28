# Behmanesh Index Ontology (BIO) v1.0

**هستی‌شناسی رسمی شاخص بهمنش**  
**نسخه:** 1.0  
**سازگار با:** CORE_BEHMANESH v1.0 + Behmanesh Index v3.4

---

## ۱. مقدمه

BIO v1.0 چارچوب مفهومی استاندارد برای تمام تحلیل‌های شاخص بهمنش است و امکان تکرارپذیری، ماشین‌خوانی و گسترش آینده را فراهم می‌کند.

---

## ۲. کلاس ریشه
**BehmaneshEntity** — هر موجود تحلیلی (Person, Account, Thread, ScientificPaper, Idea و غیره)

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

### CoreNode
- MechanisticNode
- WorldviewNode
- StrategicNode

### Relation
- TemporalEdge (Longitudinal)
- CausalEdge
- FeedbackLoop
- LeveragePoint
- ContradictionEdge

### EvaluationCriterion (با وزن)
- ConditionalDepth → ۲۲٪
- LongitudinalCoherence → ۱۸٪
- AuthenticEthicalLayer → ۱۸٪
- CreativeValueAdd → ۱۷٪
- StrategicDepth → ۱۲٪
- InterdisciplinaryBreadth → ۸٪
- AntiPerformativeDrift → ۵٪

---

## ۴. ماژول علمی (ScientificTextAnalysis)

- DisciplinaryDomain (Physics, Biomedical, Economics, AI و غیره)
- MethodologicalStandards (CONSORT, PRISMA, Falsifiability و غیره)
- ScientificClaimType
- ScientificQualityCriteria
- ScientificUncertainty

---

## ۵. Claim Classification
- [FACT]
- [INFERENCE]
- [HYPOTHESIS]
- [SPECULATION]

---

## ۶. روابط کلیدی
- `hasTheme`, `hasCoreNode`, `belongsToLayer`, `hasConfidence`, `hasLongitudinalWeight`

---

**این ontology پایه تمام تحلیل‌های آینده شاخص بهمنش خواهد بود.**

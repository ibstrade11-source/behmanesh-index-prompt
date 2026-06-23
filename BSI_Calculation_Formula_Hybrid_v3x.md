# فرمول محاسبه شاخص بهمنش (BSI) - Hybrid v3x

**نسخه:** hybrid_v3x.1  
**بر اساس:** SOP v3.4.2 + CORE_BEHMANESH  
**تاریخ:** ۱۴۰۵/۰۴/۰۲  
**هدف:** Operationalization کامل معیارها برای تکرارپذیری و اجرای استاندارد

---

## ۱. فرمول‌های کلی محاسبه

### فرمول خطی (توصیه‌شده برای traceability)
```math
BSI = \sum_{i=1}^{7} w_i \times D_i \times (1 - \overline{EIG})
فرمول غیرخطی (حرفه‌ای - penalize شدید ضعف‌ها)
BSI = 100 \times \prod_{i=1}^{7} (D_i / 100)^{w_i} \times (1 - \overline{EIG})
EIG_avg: میانگین Epistemic Integrity Gap از schemaهای مربوطه (برای adjustment عدم قطعیت).
۲. وزن‌های نهایی (v3x)
#
معیار (D_i)
وزن
1
Predictive Depth
0.23
2
Longitudinal Coherence
0.19
3
Ethical Verifiability
0.14
4
Depth Over Volume (کمتر اما عمیق‌تر)
0.18
5
Creative Value Add
0.09
6
Multidisciplinary Rigor
0.10
7
Anti-Performative Resistance
0.07
مجموع وزن‌ها = 1.00
۳. Operationalization کامل معیارها (sub-metrics)
۱. Predictive Depth (وزن: 0.23)
D1 = 0.35×Causal_Link_Density + 0.25×Testable_Predictions + 0.25×Counterfactual_Resilience + 0.15×Longitudinal_Accuracy
۲. Longitudinal Coherence (وزن: 0.19)
D2 = 0.40×Trajectory_Stability + 0.30×Contradiction_Resolution_Rate + 0.20×Stable_Nodes_Consistency + 0.10×Theme_Evolution
۳. Ethical Verifiability (وزن: 0.14)
D3 = 0.40×Value_Hierarchy_Consistency + 0.30×Anti_Performative_Score + 0.20×Ethical_Provenance + 0.10×Human_Alignment
۴. Depth Over Volume (کمتر اما عمیق‌تر) (وزن: 0.18)
D4 = 0.30×Mechanistic_Depth + 0.25×Evidence_Quality_Density + 0.20×Conditional_Reasoning_Strength + 0.15×Insight_Compression_Ratio + 0.10×Layered_Analysis_Quality
۵. Creative Value Add (وزن: 0.09)
D5 = 0.40×Novel_Connections + 0.35×Cross_Domain_Synthesis + 0.15×Generative_Capacity + 0.10×Originality_Score
۶. Multidisciplinary Rigor (وزن: 0.10)
D6 = 0.45×BIO_Ontology_Coverage + 0.30×Concept_Graph_Density + 0.15×Cross_Field_Integration + 0.10×Method_Diversity
۷. Anti-Performative Resistance (وزن: 0.07)
D7 = 0.50×Claim_Classification_Purity + 0.30×Implicit_Assumption_Exposure + 0.20×Audience_Pleasing_Detection

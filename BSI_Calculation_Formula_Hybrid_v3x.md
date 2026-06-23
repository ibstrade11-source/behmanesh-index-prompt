# BSI Hybrid v3x — مشخصات کامل و عملیاتی

**نسخه:** hybrid_v3x.1  
**بر اساس:** SOP v3.4.2 + CORE_BEHMANESH  
**تاریخ:** ۱۴۰۵/۰۴/۰۲  
**هدف:** استانداردسازی کامل BSI به عنوان Meta-Analytical Reasoning Framework

---

## ۱. Core Analysis Schema (اسکلت اصلی)

```json
{
  "schema_version": "hybrid_v3x.1",
  "bsi_version": "hybrid_v3x",
  "analysis_id": "string",
  "timestamp": "ISO8601",
  "source_metadata": { "content_id": "string", "author": "string", "platform": "string" },
  "core_worldview": { ... },
  "manifest_layer": {},
  "latent_layer": {},
  "meta_layer": {},
  "bsi_scoring": {},
  "epistemic_integrity": {},
  "executive_summary": "string"
}

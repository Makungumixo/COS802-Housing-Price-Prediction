# Data provenance

Ames Housing: 2,930 residential sales in Ames, Iowa, with 82 columns in the tab-delimited raw file. Target: SalePrice (USD). Order and PID are identifiers excluded from prediction.

Reference: De Cock, D. (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education, 19(3). https://doi.org/10.1080/10691898.2011.11889627

The raw file is preserved from the project Drive dataset. This repository does not assert a new dataset license. Consult the original publication and source terms for reuse.

`splits/` preserves row indices and development folds (seed 16153970); keep raw row ordering unchanged. `processed/` contains exported analysis results, including held-out predictions/diagnostics. These are evidence, not additional training data.

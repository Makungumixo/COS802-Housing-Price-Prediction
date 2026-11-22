# Makungu Ndlovu | COS802 presentation rehearsal

Aim for 6:35, leaving 25 seconds before the compulsory 7:00 stop. The times are rehearsal targets, not a measured delivery. Practise once aloud without reading. If running late at slide 5, omit the bootstrap explanation and retain the price-band comparison. Allow three minutes for questions.

## Slide 1

0:00–0:30. Imagine two homes with the same living area. One has much better materials and finish. Should a model value those extra square feet in the same way? That question motivated my project. I’m Makungu Ndlovu. I studied whether combining familiar property characteristics helps predict sale prices and whether the resulting model can explain what it uses.

## Slide 2

0:30–1:20. My target is the price a buyer actually paid, in dollars. A prediction based on a listing's asking price would answer a different question. I compared the information already in assessor records with features that represent a housing analyst's intuition. The example I will return to is quality multiplied by above-ground living area. A second example is total floor area. A flexible model might learn those relationships on its own, so there is no guarantee that adding them helps. The experiment asks whether they reduce errors, for which model, and where the estimates still go wrong.

## Slide 3

1:20–2:25. I used Dean De Cock’s Ames Housing data: 2,930 residential sales in one Iowa city between 2006 and 2010. The 82 columns include the sale price and two identifiers, which I excluded from the predictors. I reserved 586 homes for a final test. The other 2,344 were used for development, with the same five validation folds for each comparison. Within each fold the preprocessing learned only from the training portion. That matters for imputation and categorical encoding. For example, no garage is an observed property characteristic; it is different from a garage with an unknown construction year. I used dollar RMSE to choose configurations because large valuation misses matter, and MAE to describe average absolute error.

## Slide 4

2:25–3:40. Read across each row: the first column uses original features, the second includes the engineered ones. These are average development errors on the same five folds. Lower is better. Random forest improved by around 677 dollars in RMSE. XGBoost improved by around 441 dollars, or 1.95 percent. Yet Ridge moved in the opposite direction: its RMSE rose even though its average absolute error fell. That is why I would not claim that feature engineering always helps. The model families respond differently, and the metric matters. Engineered XGBoost had the lowest development RMSE among these configurations, so I selected it before looking at final test performance.

## Slide 5

3:40–4:50. On the 586 held-out properties, the frozen model’s average absolute miss was 13,885 dollars. RMSE was higher at 25,354 dollars, which tells us that some larger misses carried considerable weight. R squared was about 0.90: this measures explained variation, not the percentage of homes priced correctly. The bootstrap interval for RMSE was roughly 18,200 to 34,400 dollars, so the point estimate is not precise to the nearest dollar. The most expensive quarter had an average absolute error of 24,560 dollars, compared with 11,664 dollars in the lowest quarter. This is dollar error; it does not by itself establish worse percentage accuracy.

## Slide 6

4:50–6:20. The strongest explanation from SHAP was the interaction between overall quality and living area, followed by total floor area. SHAP describes the fitted model, so I checked the interpretation against an experiment: I removed both features while holding the XGBoost configuration and development folds fixed. RMSE rose by 4.35 percent. That is a different comparison from the 1.95 percent earlier, which compared the selected configurations for the two feature sets. The evidence suggests these features are useful together. It does not tell us how much a renovation would cause a sale price to rise. Quality, size and their product share information. There are two further limits. The sample represents one historical market, and some transaction details may be unavailable when a buyer first requests an estimate. Removing sale type and condition changed development RMSE by about 0.32 percent, but that is only a sensitivity check. My next test would use a later period or another city with information known at valuation time. My contribution is a comparison that shows both where feature engineering helps and where substantial errors remain.

## Slide 7

6:20–6:35. These are the dataset and method references. The project notebooks retain the split, comparisons and diagnostic results. Thank you.

## Examiner questions: lead with the short answer

**Why RMSE instead of MAE?** RMSE penalises large dollar misses more heavily and was fixed before model selection. MAE answers how far a prediction misses on average, so I report both. R² compares squared error with a mean-price benchmark.

**What was learned beyond which model won?** The same engineered inputs reduced tree-model RMSE but raised Ridge and ordinary linear regression RMSE. A feature can make the typical miss smaller yet leave a model more exposed to large misses.

**Why do the improvements of 1.95% and 3.75% differ?** The first compares selected original and engineered XGBoost configurations; those configurations can have different hyperparameters. The second removes all engineered features while keeping the engineered winner's settings fixed. They answer different questions and use different denominators.

**Could sale details leak information?** A completed sale's type and condition may be unavailable for a live valuation. Removing both raised development RMSE from $22,195 to $22,265, about 0.32%. The model should be evaluated with timestamped inputs before deployment.

**Is the quality interaction causal?** No. SHAP allocates a fitted prediction among inputs. Correlated inputs can share attribution. Removal experiments measure prediction changes, not what a renovation would cause.

**Can this be used in South Africa?** The random split tests similar historical Ames sales. A different city or later period requires new local sales, time-based validation and recalibration.

**How certain is the result?** The approximate bootstrap interval for test RMSE is $18,165–$34,407. It describes variation across resamples of this test set, not performance in a new market.

**Where did it struggle?** On 146 homes in the highest actual-price quartile, MAE was $24,560; on 147 homes in the lowest, it was $11,664. Absolute error is larger at the top. No percentage-error result is inferred from that.

## Logistics

Session, room and slot: unconfirmed. The course schedule was not included with the template. Once confirmed, join ten minutes early. Test screen sharing, microphone and slide advance. Open the local slide PDF before joining. The announced submission deadline was 11 November 2026 at 23:59; verify late-submission arrangements and the official upload link. Saving to project Drive is not course submission.


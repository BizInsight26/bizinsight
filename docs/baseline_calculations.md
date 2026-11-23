
# BizInsight — Manual Baseline Calculations

## 1. Baseline Prediction Method

BizInsight uses a simple historical average to predict next-day sales.

The baseline is non-AI and does not require model training.

Formula:

Predicted Sales = Total Valid Sales / Number of Valid Days

Only records where the store is open and sales are greater than zero are included.

## 2. Store 1 — Manual Calculation

Historical sales:

1000, 1200, 1100, 1300, 900, 1400, 1000, 0, 1500, 1200

The day with zero sales is excluded because the store was closed.

Valid sales:

1000, 1200, 1100, 1300, 900, 1400, 1000, 1500, 1200

Total sales = 10,600

Valid days = 9

Predicted sales = 10,600 / 9 = 1,177.78

## 3. Store 2 — Manual Calculation

Valid sales:

2000, 2200, 2100, 2300, 1900, 2400, 2000, 2500, 2200

Total sales = 19,600

Valid days = 9

Predicted sales = 19,600 / 9 = 2,177.78

## 4. Store 3 — Manual Calculation

Valid sales:

500, 600, 550, 650, 450, 700, 500, 750, 600

Total sales = 5,300

Valid days = 9

Predicted sales = 5,300 / 9 = 588.89

## 5. Expected vs Actual Results

| Store | Expected Prediction | Actual Prediction | Result |
|---|---:|---:|---|
| Store 1 | 1,177.78 | 1,177.78 | PASS |
| Store 2 | 2,177.78 | 2,177.78 | PASS |
| Store 3 | 588.89 | 588.89 | PASS |

All baseline predictions match the manual calculations.

## 6. Conclusion

The non-AI baseline produces correct and reproducible results on the synthetic dataset.

These calculations demonstrate that BizInsight can generate simple sales predictions without using Machine Learning.

The baseline provides a reference for evaluating more advanced forecasting models in later development.

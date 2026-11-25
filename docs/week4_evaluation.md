# BizInsight — Results, Metrics, and Evaluation

## 1. Selected Evaluation Metrics

BizInsight predicts daily store sales, which is a numerical value. Therefore, regression evaluation metrics are more appropriate than classification metrics such as accuracy, precision, recall, or F1-score.

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted sales.

A lower MAE means that predictions are closer to actual sales values.

### Root Mean Squared Error (RMSE)

RMSE measures prediction error while giving greater importance to large mistakes.

This is useful because large forecasting errors could negatively affect business planning.

## 2. Previous Evaluation Results

| Metric | Non-AI Baseline | Decision Tree |
|--------|----------------:|--------------:|
| MAE    | 2199.64.        | 1880.80       |
| RMSE   | 3009.76         |  2622.34      |

The Decision Tree reduced MAE by approximately 14.5% and RMSE by approximately 12.9% compared with the baseline.

These results were obtained from the earlier model evaluation using historical Rossmann sales data.


## 3. Error Analysis

The Decision Tree model achieved an MAE of 1880.80 and an RMSE of 2622.34.

This means that the model's predictions differed from actual daily sales by approximately 1880.80 sales units on average.

The RMSE is higher than the MAE, indicating that some predictions have larger errors.

### Possible Sources of Prediction Errors

1. Promotions: Promotional activities may cause sudden changes in sales.

2. Holidays: Customer shopping behavior may change during holidays.

3. Store Differences: Stores may have different sales patterns depending on their characteristics.

4. Seasonal Changes: Sales may increase or decrease during different months.

### Comparison with the Baseline

The Decision Tree achieved lower prediction errors than the non-AI baseline.

This indicates that the model can capture relationships between store characteristics, dates, promotions, and sales more effectively than the baseline.

However, the model is not perfectly accurate, and predictions should be treated as estimates rather than guaranteed sales values.



### Practical Error Analysis Results

The Decision Tree model was evaluated using 58,611
testing records.

The following results were obtained:

- Mean Absolute Error: 1880.80
- Root Mean Squared Error: 2622.34
- Median Absolute Error: 1438.52
- Maximum Absolute Error: 35974.48

The largest prediction error occurred when actual
sales were 41551.00, while the model predicted
5576.52.

All ten of the largest prediction errors were
underestimations of actual sales.

The actual versus predicted sales graph also showed
that the model generated similar predictions for
several records despite significant differences
in actual sales.

These findings suggest that the current Decision
Tree model has difficulty predicting exceptionally
high sales values.

Future improvements could include additional
input features, hyperparameter optimization,
and more advanced regression models such as
Random Forest.


## 4. Edge Cases

BizInsight was tested with several unusual input situations to evaluate the reliability of the prediction workflow.

### Case 1: Invalid Store ID

Input: Store ID = 2000

Expected: The system rejects the input because valid store IDs range from 1 to 1115.

Observed: An appropriate validation error was displayed.

Result: PASS

### Case 2: Missing Date

Input: No date selected

Expected: The system prevents prediction and requests a valid date.

Observed: The message "Error: Please select a valid date." was displayed.

Result: PASS

### Case 3: Model Prediction Failure

Input: Valid store and date, with a simulated model failure.

Expected: The application displays an error instead of crashing.

Observed: The application displayed "Prediction failed: Simulated model prediction failure".

Result: PASS

### Case 4: Recovery After Failure

Input: Restore the original prediction function and submit valid input.

Expected: The application produces a normal prediction.

Observed: The application successfully predicted daily sales of 9491.98.

Result: PASS

### Summary

All four exceptional and recovery scenarios passed during Week 3 testing.

These tests demonstrate that BizInsight handles invalid inputs and simulated model failures without terminating the interface.

However, they do not establish prediction accuracy for unusual sales patterns.


### Forecasting Edge Cases

The testing dataset was divided into three sales
categories using the 10th and 90th percentiles.

- Low Sales: 3949 or below.
- Normal Sales: Between 3949 and 11013, excluding
  both thresholds.
- High Sales: 11013 or above.

| Category.    | Records | MAE     |
|--------------|--------:|--------:|
| Low Sales    | 5862    | 2543.32 |
| Normal Sales | 46885   | 1378.75 |
| High Sales   | 5864    | 5232.66 |

The results show that the Decision Tree performs
best under normal sales conditions.

The model tends to overestimate unusually low sales
and underestimate unusually high sales.

High sales records produced the largest average
prediction error.

This is an important limitation because unexpected
sales peaks may influence inventory management,
staff scheduling, and financial planning.

Future improvements should focus on reducing
prediction errors during extreme sales conditions.

These categories were defined for retrospective
evaluation using actual sales values. They are not
known in advance when generating new predictions.



## 5. Technical Limitations

Although BizInsight can generate daily sales predictions, the current prototype has several limitations.

### 1. Historical Dataset

The model was trained using historical Rossmann sales data from 2013 to 2015.

Customer behavior, market conditions, and shopping patterns may have changed since then. Therefore, the model's performance on recent data is unknown.

### 2. Limited Input Features

The current prototype uses 10 input features, including store ID, date information, promotions, school holidays, and store type.

Other factors, such as weather, local events, competitor activity, and product availability, are not included.

These missing factors may influence actual sales.

### 3. Prediction Accuracy

The Decision Tree model has a measurable prediction error.

Although it performed better than the non-AI baseline in the earlier evaluation, its predictions are estimates and may differ from actual sales.

### 4. Future Date Predictions

The interface allows users to select future dates.

However, the model was evaluated using historical data, so its accuracy for future years has not been established.

### 5. Prototype Interface

BizInsight currently uses a Jupyter Notebook interface built with ipywidgets.

The interface demonstrates the complete prediction workflow but is not yet a standalone web application.

### 6. Model Maintenance

The current prototype does not automatically retrain its model when new sales data becomes available.

Future versions could support periodic retraining and performance monitoring.

## Summary

BizInsight successfully demonstrates an AI-based sales prediction workflow.

However, additional data, testing, and model improvements would be necessary before using it for real business decisions.




## 6. Human Oversight

BizInsight is designed to support business owners in making decisions, not to replace human judgment.

The system generates predicted daily sales based on historical data, but the final decision remains with the business owner.

Before using a prediction, the owner should:

1. Review the predicted sales value.
2. Compare the prediction with recent actual sales.
3. Consider external factors such as holidays, local events, and promotions.
4. Investigate unusually high or low predictions.
5. Decide whether the prediction is reasonable before taking action.

Predictions should not automatically trigger financial or operational decisions without human review.

## 7. Privacy and Ethical Considerations

### Data Privacy

The current BizInsight prototype uses the publicly available Rossmann Store Sales dataset.

The forecasting model works with store-level sales information rather than individual customer identities.

Future versions using real business data should protect sensitive financial information through appropriate access controls and secure storage.

### Responsible AI

BizInsight predictions are estimates and should not be presented as guaranteed future revenue.

Users should understand that the model can make mistakes and that its accuracy depends on the quality and relevance of the training data.

### Fairness and Reliability

Different stores may have different sales patterns. A model that performs well overall may still produce larger errors for certain stores or periods.

Future evaluations should compare prediction errors across different store types, promotional conditions, and sales periods.

### Transparency

BizInsight should clearly communicate which model generates the predictions, what input information is used, and the limitations of the results.

## Summary

Human oversight, transparency, and responsible data handling are important for ensuring that BizInsight provides useful and trustworthy business insights.



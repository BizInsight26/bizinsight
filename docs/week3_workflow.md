
# BizInsight — Functional Prototype Workflow

## 1. User Input

The user enters a Store ID, selects a date, and chooses
the promotion status, school holiday status, and store type
through the Jupyter Notebook interface.

## 2. Input Validation

The application checks whether a valid date is selected
and whether the Store ID is between 1 and 1115.

If the input is invalid, an error message is displayed.

## 3. Feature Preparation

The application extracts the day of the week, month,
and day from the selected date.

The store type is converted into numerical features
using one-hot encoding. The input features are arranged
in the same order used during model training.

## 4. Sales Prediction

The application uses a previously trained Decision Tree
Regression model to predict daily sales.

The model was trained using historical data from the
Rossmann Store Sales dataset.

## 5. Output

If prediction succeeds, the application displays the
Store ID, selected date, and predicted daily sales.

For example:

Store: 1
Date: 2015-06-01
Predicted Daily Sales: 9,491.98

## 6. Error Handling

If an unexpected error occurs during prediction,
the application catches the exception and displays
an error message instead of crashing.

## 7. Testing

The prototype has been tested with:
- Valid prediction input
- Invalid Store ID
- Missing date
- Simulated prediction failure
- Recovery after a prediction failure

All five documented test cases passed.

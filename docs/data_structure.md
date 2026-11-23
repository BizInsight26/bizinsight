
# BizInsight — Data Structure and Data Dictionary

## 1. Data Structure

BizInsight uses a CSV file to store synthetic daily sales records.

Dataset: `data/synthetic_sales.csv`

Each row represents the sales activity of one store on one date.

The dataset contains three stores and ten days of sales records per store, giving a total of 30 records.

## 2. Data Dictionary

| Field | Data Type | Description |
|---|---|---|
| Store | Integer | Unique identifier of the store |
| Date | Date | Date of the sales record (YYYY-MM-DD) |
| Sales | Number | Total sales recorded on that day |
| Customers | Integer | Number of customers on that day |
| Open | Integer (0 or 1) | Indicates whether the store was open |

## 3. Data Relationships

- Each store can have multiple daily sales records.
- Each daily sales record belongs to one store.
- The combination of Store and Date must be unique.
- A store can have only one sales record per date.

## 4. Synthetic Dataset

The dataset was manually created for testing purposes.

It contains:
- Three stores with different sales levels.
- Normal daily sales records.
- Closed-store records with zero sales and customers.
- Different customer counts across stores.

No real customer information or personal data is used.

## 5. Data Validation and Preprocessing

Before calculating predictions, BizInsight:

1. Loads the CSV dataset using pandas.
2. Converts the Date field to a datetime format.
3. Checks for missing values.
4. Checks for duplicate store/date records.
5. Rejects negative sales values.
6. Checks that Open contains only 0 or 1.
7. Excludes closed stores and invalid sales records from the baseline calculation.

## 6. Non-AI Baseline

BizInsight predicts next-day sales using historical average daily sales for each store.

Formula:

Predicted Sales = Sum of Valid Historical Sales / Number of Valid Days

The baseline does not use Machine Learning.

It provides a simple, understandable prediction that can be checked manually.

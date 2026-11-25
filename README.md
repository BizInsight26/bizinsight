# BizInsight
### AI-Powered Small Business Analytics Platform

BizInsight is an AI project designed to help small business owners understand their business performance and make better decisions using data.

The platform follows three main stages:

**Analyze → Predict → Recommend**

## Project Overview

BizInsight aims to analyze historical business data, predict future sales using Machine Learning, and provide recommendations based on identified patterns and predictions.

## Main Features

- **Business Analysis:** Identify sales trends, seasonal patterns, and changes in business performance.
- **Sales Forecasting:** Predict future sales using Machine Learning models.
- **Business Recommendations:** Suggest possible actions based on predictions, historical patterns, and predefined business rules.
- **Dashboard:** Present results through charts, financial indicators, and insights.

## Technologies

- Python
- pandas and NumPy
- scikit-learn
- Matplotlib and Seaborn
- Jupyter Notebook

## Dataset

The initial implementation will use the Rossmann Store Sales dataset from Kaggle.

https://www.kaggle.com/competitions/rossmann-store-sales/data

## Project Structure

- `data/` — Raw and processed datasets
- `notebooks/` — Data exploration and ML experiments
- `src/preprocessing/` — Data cleaning and preparation
- `src/analysis/` — Business data analysis
- `src/models/` — Machine Learning models
- `src/recommendations/` — Business recommendation logic
- `app/` — Dashboard application
- `tests/` — Project tests
- `docs/` — University documentation

## Local Setup

Clone the repository and enter the project folder:

```bash
git clone https://github.com/BizInsight26/bizinsight.git
cd bizinsight
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Project Status

Currently in development.

The first implementation will focus on historical sales analysis, sales forecasting, and rule-based business recommendations.



## Week 2 — Non-AI Baseline

BizInsight includes a simple sales forecasting baseline
that uses synthetic sales data.

The baseline predicts next-day sales using the average
historical sales for each store.

Closed-store records and zero-sales days are excluded.

### Run the baseline

From the project root:

```bash
pip install -r requirements.txt
python3 src/baseline.py
```

### Run the tests

```bash
python3 tests/test_baseline.py
```

### Expected results

- Store 1: 1177.78
- Store 2: 2177.78
- Store 3: 588.89

All four automated tests should pass.

### Week 2 Documentation

- Dataset: `data/synthetic_sales.csv`
- Schema: `docs/schema.sql`
- Data model: `docs/data_structure.md`
- Manual calculations: `docs/baseline_calculations.md`
- Test log: `tests/Week2_Test_Log.csv`

## Project Status

BizInsight is currently under active development.
Completed work includes:
- Exploration and preprocessing of the Rossmann Store Sales dataset.
- Preparation of cleaned and modeling datasets.
- Design of the database schema and data dictionary.
- Creation of a synthetic sales dataset.
- Implementation of a working non-AI sales forecasting baseline.
- Manual verification of baseline predictions.
- Implementation and successful execution of four baseline tests.

Future development will focus on machine learning forecasting, business recommendations, and the dashboard.
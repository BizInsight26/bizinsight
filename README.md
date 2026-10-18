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


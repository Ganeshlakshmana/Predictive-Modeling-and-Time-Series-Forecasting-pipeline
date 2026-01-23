## 📌 Project Description

This project implements a **Predictive Modeling and Time-Series Forecasting pipeline** using real-world **Walmart retail sales data**.  
The goal is to demonstrate how machine learning models are developed, evaluated, and validated in a structured and reproducible way for both **tabular prediction** and **temporal forecasting** problems.

The project is designed to closely reflect **real industry workflows**, focusing on clean data preparation, feature engineering, proper train–test splitting, and meaningful evaluation rather than overly complex models.

---

### 🎯 Objectives

The project addresses two closely related business problems:

1. **Predictive Modeling (Regression)**  
   Predict weekly sales using external economic and seasonal features such as temperature, fuel price, CPI, unemployment rate, and holiday indicators.

2. **Time-Series Forecasting**  
   Forecast future weekly sales based on historical sales trends while strictly respecting the temporal order of the data.

---

### 🧠 Key Design Principles

- **Separation of concerns**:  
  Data loading, preprocessing, feature engineering, modeling, and evaluation are implemented as separate modules.

- **Realistic assumptions**:  
  Missing promotional (`MarkDown`) values are handled using domain knowledge, assuming missing values indicate no active promotion.

- **Correct evaluation strategy**:  
  - Regression models use train–test splits and cross-validation.
  - Time-series models use time-based splits to avoid data leakage.

- **Baseline-first approach**:  
  Simple and interpretable models are used to establish strong baselines before considering more complex approaches.

---

### 🔄 Workflow Overview

Raw Walmart Sales Data
↓
Data Validation & Cleaning
↓
Feature Engineering
↓
Regression Pipeline

Train/Test Split

Cross-Validation

MAE, RMSE, R² Evaluation
↓
Time-Series Forecasting Pipeline

Chronological Split

Trend-Based Forecasting

Forecast Error Analysis


---

### 📊 Techniques Used

- Python (pandas, NumPy)
- scikit-learn
- Linear Regression
- Feature engineering
- Cross-validation
- Error analysis (MAE, RMSE, R²)
- Time-aware train–test splitting

---

### ✅ What This Project Demonstrates

- Practical experience with **real-world retail data**
- Strong understanding of **predictive modeling vs forecasting**
- Ability to design **modular and reusable ML pipelines**
- Awareness of common pitfalls such as **data leakage**
- Clear, explainable decision-making aligned with industry practices

This project emphasizes **clarity, correctness, and reproducibility**, which are critical skills for junior machine learning and data science roles.

# 📊 E-Commerce Customer Retention & Cohort Analysis

This project analyzes customer purchasing behavior and retention rates for an online retail dataset using Python (Pandas) and Excel. The objective is to track how long customers continue to make purchases after their first transaction (Cohort Analysis).

---

## 🚀 Project Workflow & Steps
1. Data Cleaning: Loaded the dataset and cleaned missing values (filtered out rows with missing `CustomerID`).
2. Date Processing: Extracted transaction months (`InvoiceMonth`) and determined each customer's first purchase month (`CohortMonth`).
3. Cohort Index Calculation: Calculated the relative month index (`CohortIndex`) representing the age of the customer's lifecycle.
4. Pivot Table Creation: Grouped data by `CohortMonth` and `CohortIndex` to calculate unique active customers (`.nunique()`).
5. Retention Matrix Calculation: Converted absolute customer counts into percentages (%) relative to the initial month size.

---

## 📈 Results & Business Insights
![Retention Matrix Results](retention_matrix.png)
- Customer Churn: The highest customer drop-off typically occurs right after the first month (Index 1).
- Long-term Loyalty: Certain cohorts show sustained repeat purchases over a 12-month period, indicating strong brand loyalty.

---

## 🛠️ Built With
- Python (Pandas library)
- Microsoft Excel (Data inspection and validation)
import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent

# 1) Load data
df = pd.read_excel(BASE / 'online_retail_dataset_cohort.xlsx', sheet_name='online_retail')

# 2) Clean data
df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]   # remove cancelled invoices
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]       # remove returns / invalid prices

# 3) Dates and cohort month
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
df['CohortMonth'] = df.groupby('CustomerID')['InvoiceMonth'].transform('min')

# 4) Cohort index (months since first purchase)
year_diff = df['InvoiceMonth'].dt.year - df['CohortMonth'].dt.year
month_diff = df['InvoiceMonth'].dt.month - df['CohortMonth'].dt.month
df['CohortIndex'] = year_diff * 12 + month_diff

# 5) Retention matrix
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerID')

cohort_size = cohort_pivot.iloc[:, 0]
retention_matrix = cohort_pivot.divide(cohort_size, axis=0) * 100

print(retention_matrix.round(2))

# 6) Save output
retention_matrix.round(2).to_excel(BASE / 'Retention_Matrix_Python.xlsx')

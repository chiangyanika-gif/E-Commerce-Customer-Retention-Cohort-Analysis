import pandas as pd

file_path = '/Users/xiang/Documents/PROJECT/Marketing/E-Commerce Customer Retention & Cohort Analysis/online_retail_dataset_cohort.xlsx'
df = pd.read_excel(file_path, sheet_name='online_retail')

df = df.dropna(subset=['CustomerID'])

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

df['CohortMonth'] = df.groupby('CustomerID')['InvoiceMonth'].transform('min')

year_diff = df['InvoiceMonth'].dt.year - df['CohortMonth'].dt.year
month_diff = df['InvoiceMonth'].dt.month - df['CohortMonth'].dt.month
df['CohortIndex'] = year_diff * 12 + month_diff

cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerID')

cohort_size = cohort_pivot.iloc[:, 0]
retention_matrix = cohort_pivot.divide(cohort_size, axis=0) * 100

print(retention_matrix.round(2))




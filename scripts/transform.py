# transform.py
import pandas as pd
import os

df = pd.read_parquet('data/raw/sales.parquet')
result = df.groupby('producto')['venta'].sum().reset_index()

os.makedirs('data/processed', exist_ok=True)
result.to_parquet('data/processed/sales_summary.parquet')
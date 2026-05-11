import pandas as pd
import random
import os

data = {
    'producto': [random.choice(['A', 'B', 'C']) for _ in range(10)],
    'venta': [random.randint(50, 100) for _ in range(10)]
}
df = pd.DataFrame(data)

os.makedirs('data/raw', exist_ok=True)
df.to_parquet('data/raw/sales.parquet')
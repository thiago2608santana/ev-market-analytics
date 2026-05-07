import numpy as np
import pandas as pd

def insert_null_values(df: pd.DataFrame) -> pd.DataFrame:
    
    colunas_nulos = ["annual_sales_units", "customer_rating", "warranty_years", "body_type", "brand"]

    for col in colunas_nulos:
        indices_nulos = df.sample(frac=0.05).index
        
        df.loc[indices_nulos, col] = np.nan

    return df

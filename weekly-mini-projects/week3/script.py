# week 2

# import pandas as pd
# df = pd.read_csv('../../assets/datasets/credit/train.csv')
# print(df.info())

# week 3
# pip install polars

import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv('../../assets/datasets/credit/train.csv', ignore_errors=True)

print(df.describe())
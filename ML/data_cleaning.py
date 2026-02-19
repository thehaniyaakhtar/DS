# identifying missing values
import numpy as np

# Missing per column
missing_values = df.isnull().sum()
count[0:10]

# Total cells
total = np.prod(df.shape)

# Total missing values
missing = missing_values.sum()

# Percentage missing
percent = (missing/total)*100


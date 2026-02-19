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

# dropping missing values

#removing rows
data.dropna()

#removing columns
data.dropna(axis=1)

#calculating dropped columns
# cols [1]
# rows [0]
org_cols = data.shape[1]
dropped_cols = dropped.shape[1]
calc = (org_cols - dropped_cols)

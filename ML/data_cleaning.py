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
dropped = data.dropna(axis=1)

#calculating dropped columns
# cols [1]
# rows [0]
org_cols = data.shape[1]
dropped_cols = dropped.shape[1]
calc = (org_cols - dropped_cols)

# filling mising values

# replacing NaN values with 0
data.fillna(0)

# imputation techniques
# forward fill: ffill: fills downward with prev value
# backward fill: bfill: fills upward with  below value

data.fillna(method = 'ffill', axis=0).fillna(0)
# axis = 0: top to bottom, prev row

data.fillna(method = 'ffill', axis=1).fillna(0)
# axis = 1; left to right, prev col

data.fillna(method = 'bfill', axis=0).fillna(0)
# axis = 0; bottom to top; next row value

data.fillna(method = 'bfill', axis=1).fillna(0)
# axis = 1; right to left; next col value

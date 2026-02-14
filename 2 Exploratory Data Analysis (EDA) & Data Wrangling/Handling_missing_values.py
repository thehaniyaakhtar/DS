""" 
Why is a value missing?
MCAR: Missing Completely at Random
Missingness unrelated to any variable

MAR: Missing At Random
Missingness related to other observed variables

MNAR: Missing Not At Random
Missingness depends on the missing value itself
Requires deeper modeling
"""
# Mean/ Median/ Mode Imputation

from sklearn.impute import SimpleImputer
import numpy as np

X = np.array(([1], [2], [5], [np.nan]))

imputer = SimpleImputer(strategy="mean")
X_imputed = imputer.fit_transform(X)

'''
Pros: Fast, Simple
used when small % of missing values
Cons: Reduces variance artificially

Median is used if data is skewed, outliers exist.
'''

# KNN Implementation
'''
Instead of filling with global average, the values of similar rows are used
for each missing value: 
find k nearest neighbors
take avg
fill value

preserves local structure

slow for large datasets
sensitive to scaling

Must scale features before KNN
'''
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=3)
X_imputed = imputer.fit_transform(X)

# MICE (Multiple Imputation by Chained Equations)
'''
Model each feature as a function of other features

Pick column
Predict it using other columns
Fill missing values
Move to next column
Repeat

Preserves relationships between variables
Works well under MAR

Computationally heavy
Overfit small datasets
Needs tuning
'''
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer()
X_imputed = imputer.fit_transform(X)


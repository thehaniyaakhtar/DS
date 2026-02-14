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


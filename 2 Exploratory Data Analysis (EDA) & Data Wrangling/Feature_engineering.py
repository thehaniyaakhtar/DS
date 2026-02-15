'''
Feature Engineering
Transforming raw variables into representations that make patterns easier for models to learn

Scaling and Normalization
magnitude control

Scaling matters:
age: 0-100
income: 0-1000000

Distance based models will treat income far more imp because of scale
'''
'''
Standardization(Z score scaling)
x′= x−μ/σ
mean = 0
std = 1
'''

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# causes features to be centered and scaled, optimization behaves better
'''
Feature Engineering
Transforming raw variables into representations that make patterns easier for models to learn

Scaling and Normalization
magnitude control

Scaling matters:
age: 0-100
income: 0-1000000

Distance based models will treat income far more imp because of scale
'''
'''
Standardization (Z score scaling)
x′= x−μ/σ
mean = 0
std = 1
'''

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# causes features to be centered and scaled, optimization behaves better
'''
Max-Min Normalization

x′= x−min/max−min
Range = [0 ,1]
'''
from sklearn.preprocessing import MinMaxScaler
# used in neural networs and bounded features
# Tree based models do no require scaling, they split based on thresholds

'''
Encoding Categorical Variables
Models understand numbers not categories

Label Encoding
Red: 0
Blue: 1
Green: 2

Used only for ordinal categories:
low << medium << high
'''
from sklearn.preprocessing import LabelEncoder

'''
One Hot Encoding
Creates binary columns
Red → [1,0,0]
Blue → [0,1,0]
Green → [0,0,1]
Used for Nominal Categories, in linear models
'''
from sklearn.preprocessing import OneHotEncoder

# disadvantages: High cardinality: explosion of columns
# 1000 unique cities: 1000 columns

'''
Binning:
Convert continuous variables into categories
Handles non linear relationships
Reduces noise
'''
import pandas as pd
df['age_bin'] = pd.cut(df["age"], bin = 4)
#can lead to loss of info

'''
Polynomial Features
Used to model non linear relationships in linear models
If relationship is:
Y = aX² + bX + c
Linear Regression alone cannot capture it
X² is treated as a feature
Linear regression can model it
'''
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

'''
Linear models are linear in parameters, not linear in variables
By adding X², curved relationships are allowed
'''

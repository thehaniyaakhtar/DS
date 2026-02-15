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









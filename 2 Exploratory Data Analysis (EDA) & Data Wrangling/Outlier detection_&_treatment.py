'''
Outliers are values that deviate significantly from the majority of the data
Sometimes they can be errors/
the most important signals

They are context dependent
'''
'''
Z-Score Method
Method assumes approximate normal distribution
Each value is standardized
Z score tells how many SDs away a point is away from the mean
|Z| > 3, Potential Outlier, 99.7% data lies within +-3 SD
'''
import numpy as np

mean = np.mean(X)
std = np.std(X)

z_scores = (X - mean) / std
outliers = np.abs(z_scores) > 3

'''
used best when
data roughly normal
no heavy skew
few extreme points
'''
'''
IQR
Q1 = 25th Percentile
Q3 = 75th Percentile

IQR = Q3 - Q1
Lower = Q1 - 1.5 * IQR
Upper = Q3 + 1.5 * IQR
Outside points are outliers
'''

q1 = np.percentile(X, 25)
q2 = np.percentile(X, 75)
IQR = q3 - q1

lower = q1 - 1.5*IQR
upper = q3 - 1.5*IQR

outliers = (X<lower) | (X>upper)

'''
uses median based spread
robust to skew
'''

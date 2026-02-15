'''
Imbalanced data 
occurs when class distribution is skewed
Fraud Detection:
99.5%: Not Fraud
0.5%: Fraud
Model can predict "Not Fraud" always and get 99.5% accuracy, useless

Undersampling:
Reduce majority class size

Original:
10,000 majority
500 minority

After undersampling:
500 majority
500 minority

it is simple, fast
it throws aways data, can remove useful signal, risk of underfittig
'''
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

'''
Oversampling
Increases minority class size
simplest method, duplicates minority samples

it keeps all data and balances distribution
duplication can lead to overfitting risk
model may memorize minority points
'''
from imblearn.over_sampling import RandomOverSampler

res = RandomOveSampler()
X_res, y_res = res.fit_resample(X, y)
'''
SMOTE
Synthetic Minority Oversampling Technique

Doesnt duplicate minority samples, creates synthetic new ones

picks a minority point
finds k nearest minority neighbors
generates new sample along lines between them

it introduces variation, reduces overfitting
expands minority decision region
'''
from imblearn.over_sampling import SMOTE

smote = SMOTE()
X_res, y_res = smote.fit_resample(X, y)

'''
Struggles with categorical features
Fails if minority class is sparse
'''
'''
Oversampling shrinks majority cluster volume
Undersampling shrinks majority cluster
SMOTE smooths minority decision boundary
'''

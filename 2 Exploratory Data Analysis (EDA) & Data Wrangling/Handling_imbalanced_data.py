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

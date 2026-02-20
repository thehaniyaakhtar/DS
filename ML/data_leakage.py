# Data Leakage
# Training dataset is used to create a model
# same dataset is not going to be available when the model is used 
# Target Leakage
# future data (not in test dataset) is included in training data
# eg: if someone has taken an antibiotic, it must mean they might have pneumonia
# Train Test Contamination
# Happens when validation data is accidentally used during training 

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_score = cross_val_score(my_pipeline, X, y, cv = 5, scoring = 'accuracy')

print(cv_score.mean())

# RFC, run 5 fold ccv, compute accuracy and the average

# predicting who has a CC
# target variable: cardholder (0 or 1)

# seperate expenditure values
cardholders = X.expenditure[y == 1]
non_cardholders = X.expenditure[y == 0]

# percentage of zero expenditure
print("No card: {:.2f}".format((non_cardholders == 0).mean()))
print("Card: {:.2f}".format((cardholders == 0).mean()))

# almost all cardholders have some expenditure 
# non ch have 0 expenditure 

# remove leaky features
leaks = ['expenditure', 'share', 'active', 'majorcards']
# detects leakage by analyzing exp. column
# observes that non holders: 0 expenditure...
X2 = X.drop(leaks, axis=1)
# removes leaky columns

# retrain model
cv_scores = cross_val_scores(
    my_pipeline,
    X2,
    y,
    cv = 5,
    scoring='accuracy'
)

print("Accuracy without leakage: {:.4f}".format(cv_scores.mean()))

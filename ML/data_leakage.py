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

# RFC,, run 5 fold ccv, compute accuracy and the average

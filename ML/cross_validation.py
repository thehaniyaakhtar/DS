# Cross Validation
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score

# create a function to build a preprocessing + pipeline
# builds a preprocessing + model pipeline
# returns MAE
def get_score(n_estimators):
    # number of parameter values x number of folds
    # trains and evaluates a model using specific no. of trees
    
    my_pipeline = Pipeline(steps=[
        # entire pipeline is refit from scratch inside each fold
        # imputation + training happens only using training fold data
        # no data leakage occurs
        # each fold refits from scratch
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(
            n_estimators = n_estimators,
            random_state = 0
        ))
    ])
    
    scores = -1 * cross_val_score(
        # scikit learn assumes higher scores are better
        # MAE is a loss function, returns negative MAE
        # multiply by -1 to make it positive
        my_pipeline,
        X, y, 
        cv = 3, # split the dataset into k folds, each fold becomes validation set at a time, the other 2 train
        scoring = 'neg_mean_absolute_error'
    )
    
    return scores.mean()
    
# testing different number of trees
results = {}

for i in range(1, 9):
    results[50*i] = get_score(50*i)
    # 50, 100, 150, 200, 250, 300, 350, 400 tree counts are tested
    
# selecting the best parameter
# find the number of estimators with the lowest MAE
n_estimators_best = min(results, key = results.get)

# more reliable estimate
# uses data more efficiently
# better for smaller datasets
# better for hyperparameter tuning

# train/test is better for very large datasets
# final evaluation after tuning
# quick exp

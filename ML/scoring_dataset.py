# scoring a dataset using a model
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    # uses 10 decision trees
    # random_state = 0 ensures reproducibility
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# identifying columns with missing values
cols_missing_values = [
    col for col in X_train.columns
    if X_train[col].isnull().any()
]

# dropping columns with missing values
reduced_X_train = X_train.drop(cols_missing_values, axis = 1)
reduced_X_valid = V_valid.drop(cols_missing_values, axis = 1)

# scoring after dropping columns
print(score_dataset(
    reduced_X_train,
    reduced_X_valid,
    y_train,
    y_valid
))
# Train model without columns containing missing values

# Imputation
# Replacing missing values with meaningful estimates instead of deleting data
from sklearn.impute import SimpleImputer

# Create imputer object
my_imputer = SimpleImputer()
# default strategy: mean
# learns missing value patters from training data

# imputing training data
imputed_X_train = pd.DataFrame(
    my_imputer.fit_transform(X_train)
)

# imputing validation data
imputed_X_valid = pd.DataFrame(
    my_imputer.transform(X_valid)
)

# transform() prevents data leakage

# restoring column names
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

# scoring after imputation
print(score_dataset(
    imputed_X_train,
    imputed_X_valid,
    y_train,,
    y_valid
))

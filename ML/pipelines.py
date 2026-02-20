# pipelines
# a pipeline automates preprocessing + modeling into one object
# a pipeline bundles everything togetehr instead of doing it manually
# imputation,  encoding, scaling, modeling
# they prevent data leakage
# reproducible and less manual mistakes
# makes ml production ready

# step 1: define preprocessing steps
# handling of numerical and categorical features are defined

from sklearn.compose import columnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# pipelne to handle numeric and categorical cols
# numeric value missing is replaced with 0
numerical_transformer = SimpleImputer(strategy = 'constant')

# fill missing values with common category
# convert categories into one hot encoded columns
categorical_transformer = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('one_hot', OneHotEncoder(handle_unknown='ignore'))
])

# combine them
preprocessor = ColumnTransformer(
    transformer = [
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
])
# apply numeric/ categoric cleaning to numeric/ categoric columns
# merge

# define model

# create and evaluate pipeline
from sklearn.metrics import mean_absolute_error

# creates a single workflow
my_pipeline = pipeline(steps=[('preprocess', preprocess),
('model', model)
])

my_pipeline.fit(X_train, y_train)
preds = my_pipeline.predict(X_valid)

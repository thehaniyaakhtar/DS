# handling categorical values
# represent labels/ categories

# identifying categorical columns
s = (X_train.dtypes == 'object')

# Listing Categorical COlumns
object_cols = list(s[s].index)
print(object_cols)

# s is a Boolean Series (True/False for each column)
# s[s] means: keep only the True entries

# dropping categorical variables
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

# ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
ordinal = OrdinalEncoder()

label_X_train[object_cols] = ordinal.fit_transform(X_train[object_cols])

label_X_valid[object_cols] = ordinal.transform(X_train[object_cols])

# replaces categorical columns with a single column using numerical columns
# each category has a unique value assigned
# existing columns are replced, no new ones are added
# works well for high cardinality if categorical order makes sense
# if not encoding introduces misleading patterns in ML model

# one hot encoding
# creates a new column for each unique category
# categorical data turns into multiple binary columns
# it helps avoid numerical relationships between categories which can be misleading
'''
dataset: 10000 rows
100 unique categories ~ 100 new columns ~ 99 zeroes, 1 one
1 original column is removed
100 new are added: net +99
for 10000 rows: 10000*99
it is thus only appropriate for smaller cardinalities
'''

# importing encoder
from sklearn.preprocessing import OneHotEncoder

# creating encoder
OH_encoder = OneHotEncoder(
    handle_unknown = 'ignore',
    sparse = False
)
# handle unknown: if a category was seen in training data and not in validation, ignore it, dont throw error, rurns into all 0s
# sparse = False 
# By default OH returns sparse matrix
# Sparse matrix stores only non zero values
# thus sparse = False returns normal dense NumPy array

# Fit and Transformer
OH_cols_train = pd.DataFrame(
    OH_encoder.fit_transform(X_train[object_cols])
)

# fit(): learns unique categories from train data
# transform(): converts categories to binary columns
# pd.DataFrame: converts numpy array into datafram

# restoring index as original index is lost 
# to ensure rows align correctly
OH_cols_train.index = X_train.index

#applying to validation
OH_cols_valid = pd.DataFrame(
    OH_encoder.transform(X_valid[object_cols])
)

OH_cols_valid.index = X_valid.index

# Removing original categorical columns
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

# combine numeric cols
# new encoded categorical columns

# convert column names to string
OH_X_train.columns = OH_X_train.columns.astype(str)
# some models expect column names to be strings



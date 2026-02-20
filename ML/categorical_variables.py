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

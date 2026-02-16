#loading data
df = pd.read_csv('file_path')

#understanding data
#shows no. of rows and columns, names of cols, data type, null count
df.info()

#understand data distribution numerically
df.describe()

#returns the no of rows and columns in a df
df.shape

# first/last 5/n rows 
df.head()
df.tail(n)

# returns column names
df.columns

# unique values
df.nunique()

# number of null values in each col
df.isnull().sum()

# unique values in a column
df['column'].value_counts()

# correlation matrix from -1 to 1
df.corr()

# parenthesis used in methods not attributes
# methods are actions on dataframes involving computation, require () to eexecute (verb)
# attributes are properties that store info (noun)

# building a model
# data selection
y = df["target_col"]
X = df[["", "", ""]]
'''
one col as series: df[col]
one col as datafram: df[[col]]
multiple cols: df[[col, col, col]]

# defining and fitting a model
from sklearn.tree import DecisionTreeRegressor
df_model = DecisionTreeRegressor(random_state=1)
df_model.fit(X, y)

# predict results
df_model.predict(X)
df_model.predict(X.head())

#model validation
# calculating error
from sklearn.metrics import mean_absolute_error
pred_data = df_model.predict(X)
mean_absolute_error(y, pred_data) # models pred values & actual values

# train and testing data
from sklearn.model_selection import train_test_split
train_X, val_x, train_y, val_y = train_test_split(X, y, random_state = 0)

# random_split
#controls randomness
#ensures consistency
# random_state = 42 doesnt matter
# ensures split is same, else the result changes everytime

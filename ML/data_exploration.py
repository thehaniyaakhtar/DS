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

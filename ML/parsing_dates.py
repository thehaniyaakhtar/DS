# working with data 
# dates are stored as strings
# they must be parsed into datetime format

# checking data type
df['date'].dtype

# convert to datetime
df['parsed'] = pd.to_datetime(df['date'])

#specific format faster, more accurate
df['parsed'] = pd.to_datetime(
    df['date'],
    format = '%m/%d/%y'
)

# handling multiple data formats
df['date_parsed'] = pd.to_datetime(
    df['date'],
    infer_datetime_format = True
)
# pandas guesses the date format
# it is slower, not always accurate

# extracting info from dates
day_of_month = df['data_parsed'].dt.day
month = df['date_parsed'].dt.month
year = df['date_parsed'].dt.year
day_of_week = df['date_parsed'].dt.dayofweek 

# plotting date based features
# dropping NA
day_of_month = day_of_month.dropna()
sns.distplot(day_of_month, kde = False, bins=31)

# one bin per possible day
# frequncy of events per day

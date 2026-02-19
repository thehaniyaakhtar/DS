#  scaling: changing the range of features values
# data distribution shape/ relationship does not change
# chnges the magnitude
# eg: [0, 10000] to [0, 1]
# important for distance based algos, SVM, KNN
# as larger features may end up dominating model

# min max scaling
# rescales data to a fixed range usually [0, 1]
# preserves the original distribution shape
# min value: 0, max value: 1
# sensitive to outliers
# relative distances between points remain same
# sensitive to outliers
data = dataset_name[['specific_col']]
scaled_data = minimax_scaling(data, columns=['specific_col'])
# converts values range to [0, 1]

#confirm scaling
print("Original data", data.head())
print("Min Value", float(data.min()))
print("Max Value", float(data.max()))

# standardization 
# centers data around a mean = 0 
# scales using std dev
# mean becomes 0
# std dev bcomes 1
# handles outliers better than min max scaling

# K Nearest Neighbors (KNN)
# Distance based classification algorithm
# classifies data point based on nearest neighbors
# scaling is imp as distance metrics are sensitive to scale
# without it, larger features will dominate

# normalization
# transformation process that reshapes data, follows normal distribution
# it has a bell shaped curve
# symmetric around mean
# many ML models assume data is normally distributed 
# it reduces skewness, handles extreme values

# Linear Distribution Analysis
# supervised classification algorithm
# dimensionality reduction method
# finds the best linear combination of features
# seperates classes as much as possible
# maximizes distances between classes
# minimizes spread with each class
# assumes data is normalised
# it improves class seperation

# box cox transformation
# applies power transformation to skewed data
# makes data more normally distributed
# only works for positive values
# reduces skewness
# spreads data more evenly
# it improves ML models performance
# works for positive data only

normalized_data = stats.boxcox(org_data)
# stats.boxcox() makes data closer to gaussian dist
# it returns a tuple, not a single array
# (normalized_values, lambda_value)
# normalized_Data[0]: contains transformed data
# normalized_data[1]: comtains lambda values used in transformation

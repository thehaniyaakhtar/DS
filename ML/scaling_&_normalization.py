# scaling and normalization
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

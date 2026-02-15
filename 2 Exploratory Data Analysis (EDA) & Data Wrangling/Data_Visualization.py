'''
Histograms
Shows the frequency of values in bins
Choose appropriate bin size (too many = noisy, too few = oversmoothed)
Compare groups with transparency
'''
df = pd.read_csv("data.csv")

plt.figure()
plt.hist(df["feature"], bins = 30)
plt.xlabel("Feature")
plt.ylabel("Frequency")
plt.title("Histogram of Feature")
plt.show()

# with KDE
sns.histplot(df["feature"], bins = 30, kde = True)
plt.title("Histogram")
plt.show()

#comparison by category
sns.histplot(data=df, x="Feature", hue="Category", kde=True, element="step")
plt.show()

'''
Box Plots
where is the median
the spread of data
and are there outliers

used for comparing distributions across categories
avoided when dataset is v small
'''
#single variable
sns.boxplot(y=df["feature"])
plt.title("")
plt.show()

#grouped by category
sns.boxplot(data=df, x="", y="")
plt.show()

#horizontal version
sns.boxplot(x=[""])
plt.show()

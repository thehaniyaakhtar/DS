## Descriptive vs. Inferential statistics
- Descriptive Stats: summarizing and describing data
- Does not try to generalize/predict
- Only answers how the dataset looks like

1. Measures of Central Tendency: center of data
   - Mean: Average; balancing point of dataset
        - Uses every point in dataset
        - Sensitive to outliers
        - Minimizes total squared distance/total squared error, thus used in Regression
   - Median: Middle Value
        - Ignores magnitude
        - Robust to outliers
        - Better for skewed data
   - Mode: Most frequent value
        - Data is categorical
        - popularity matters
     
2. Measures of Spread/Dispersion: How spread out is the data
   - Range: Max - Min
        - Extremely sensitive to outliers
   - Variance: Average: Average Squared deviation
        - Avg squ distance from mean, removes -ve signs
        - squ penalize large deviations heavily
        - Measures how far data spreads around the mean
   - Standard Deviation: Typical distance from mean
        - how far away a typical observation is form the mean
        - In a normal distribution:
             - 68% within 1 SD
             - 95% within 2 SD
             - 99.7% within 3 SD
   - IQR: Middle 50% spread
        - = Q3 - Q1
        - Robust

   - Dispersion matters: High variance = unstable model
                         Low Variance = consistent behavior

3. Distribution Shape:
   - Skewness (left or right tail): Assymetry of distribution
        - Symmetric(Skew = 0) Median ~ Mean ~ Mode
            - Normal Distribution
        - Positive Skew (Right Skew) Mean > Median
            - Outliers on the high end
        - Negative Skew (Left Skew) Median > Mean
   - Kurtosis (weight of tail)
        - NOT about the peak height, about outliers
        - Mesokurtic (Normal)
        - Leptokurtic (High Kurtosis) 
             - Heavy tails
             - More extreme outliers
             - Higher risk
        - Playkurtic (Low Kurtosis)
             - Light tails
             - Fewer outliers
        - High Kurtosis: finance: extreme risk events
                         ML: outlier sensitivity  

- Inferential Statistics: Using a small sample to make conclusions about a larger population
- Entire population cannot be measured, a sample is analyzed and the population is infered

1. Estimation:
   - Estimating poplulation parameters from a sample.

2. Hypothesis Testing
   - Make a claim (Null Hypothesis)
   - Collect sample data
   - Calculate probability (p-value)
   - Accept/Reject claim

3. Regression
   - Poplulation slope is estimated
   - Significance of features
   - Confidence intervals of coefficients
  
## Probability distributions (Normal, Binomial, Poisson, Exponential, Bernoulli)

1. Bernoulli Distribution: single binary outcome
      - Discrete variables
      - 2 possible outcomes 0 or 1
      - p: prob of success; mean = p; variance = p(1-p)

2. Normal Distribution: continuous variable
      - models values that can take any real number.
      - appears when small independent random effects combine, due to CLT
      - Bell Shaped, symmetric, mean = median = mode
      - mean = center; variance = spread

3. Binomial Distribution: Discrete Variables; counts number of succeses in n trials
      - Discrete variables, counts number of successes in n trials
      - n: no. of trials; p: prob of success
      - mean: np; variance: np(1-p)

4. Poisson Distribution: Discrete, counts number of events in fixed interval
      - How many times is something happening in a fixed space or time
      - λ (lambda) = average rate of events; Mean = λ Variance = λ; equality is very important.

5. Exponential Distribution: Continuous variables
      - How long until the next event?
      - λ: rate parameter; mean = 1/λ

## Law of Large Numbers (LLN)
      - As sample size n -> ∞
      - Sample Mean -> Population Mean
      - Averages converge

## Central Limit Theorem (CLT)
      - What does the distribution look like
      - Even if original data is skewed, ,uniform, exponential, weird shaped,
      for many samples of n, computing means, plotting them, as size of n becomes large, the means form a normal distribution.

#### LLN: with more data, estimates stabilize
#### CLT: with more data, sampling distribution becomes normal

## Hypothesis Testing
Is an effect real or just random noise

      


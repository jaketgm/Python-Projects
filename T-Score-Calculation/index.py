import scipy.stats as stats

# Given data
population_mean = 233.35
sample_mean = 225
sample_std_dev = 21.53
sample_size = 16

# Calculate the test statistic (t-score)
standard_error = sample_std_dev / (sample_size ** 0.5)
t_score = (sample_mean - population_mean) / standard_error

# Calculate the degrees of freedom
degrees_of_freedom = sample_size - 1

# Calculate the two-tailed p-value
p_value = 2 * (1 - stats.t.cdf(abs(t_score), df=degrees_of_freedom))

# Round the answers to three decimal places
t_score = round(t_score, 3)
p_value = round(p_value, 3)

# Output the results
print("Test Statistic (t-score):", t_score)
print("Two-tailed p-value:", p_value)

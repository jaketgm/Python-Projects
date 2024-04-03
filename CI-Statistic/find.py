import scipy.stats as stats

# Given data
mean1 = 5
std_dev1 = 200
n1 = 361
mean2 = 2
std_dev2 = 185
n2 = 361

# Null Hypothesis
null_mean_diff = 0

# Calculate the z-statistic
z_statistic = (mean1 - mean2 - null_mean_diff) / ((std_dev1**2/n1 + std_dev2**2/n2)**0.5)

print(f"Z-statistic: {z_statistic:.4f}")
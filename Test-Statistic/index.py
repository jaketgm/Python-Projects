import scipy.stats as stats

# Given data
sample_mean = 1.83  # Sample mean
population_mean = 2.0  # Population mean
std_deviation = 0.473645  # Standard deviation
sample_size = 40  # Sample size

# Calculate the test statistic (z-score)
z = (sample_mean - population_mean) / (std_deviation / (sample_size**0.5))

# Define the significance levels
alpha_b = 0.01  # For part (b)
alpha_c = 0.05  # For part (c)

# Find the critical z-value for the given significance levels
z_critical_b = stats.norm.ppf(alpha_b)
z_critical_c = stats.norm.ppf(alpha_c)

# Test the claim for part (b)
if z < z_critical_b:
    print("Reject the null hypothesis at the 0.01 significance level.")
else:
    print("Fail to reject the null hypothesis at the 0.01 significance level.")

# Test the claim for part (c)
if z < z_critical_c:
    print("Reject the null hypothesis at the 0.05 significance level.")
else:
    print("Fail to reject the null hypothesis at the 0.05 significance level.")

# Print the test statistic (z)
print(f"Test Statistic (z): {z}")

# Print the critical z-values for alpha = 0.01 and alpha = 0.05
print(f"Critical z-value for alpha = 0.01: {z_critical_b}")
print(f"Critical z-value for alpha = 0.05: {z_critical_c}")
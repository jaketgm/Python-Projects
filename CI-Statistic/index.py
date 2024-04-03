import scipy.stats as stats
import math

# Given data
mean_student = 7.6
std_student = 3.6
n_student = 80

mean_faculty = 5.3
std_faculty = 3.7
n_faculty = 55

# Calculate the test statistic and critical value
alpha = 0.05
degrees_of_freedom_student = n_student - 1
degrees_of_freedom_faculty = n_faculty - 1

# Calculate the pooled standard deviation
pooled_std = math.sqrt(((std_student**2 / n_student) + (std_faculty**2 / n_faculty)))

# Calculate the test statistic
test_statistic = (mean_student - mean_faculty) / pooled_std

# Degrees of freedom for the t-distribution
degrees_of_freedom = n_student + n_faculty - 2

# Calculate the critical value
t_critical = stats.t.ppf(1 - alpha/2, degrees_of_freedom)

# Calculate the confidence interval
margin_of_error = t_critical * pooled_std * math.sqrt(1/n_student + 1/n_faculty)

lower_bound = (mean_student - mean_faculty) - margin_of_error
upper_bound = (mean_student - mean_faculty) + margin_of_error

print("95% Confidence Interval for the difference (μ1 - μ2): ({:.2f}, {:.2f})".format(lower_bound, upper_bound))
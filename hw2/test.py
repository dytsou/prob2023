import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Define the parameters
sequence_length_S3 = 10**3
sequence_length_S4 = 10**4
p_T = 0.25  # Probability of 'T', assuming equal probability for A, C, G, and T

# Calculate the number of 'T' occurrences for S3 and S4
n_S3 = sequence_length_S3
n_S4 = sequence_length_S4

# Create an array of possible values for X_S3 and X_S4
x_values_S3 = np.arange(n_S3 + 1)
x_values_S4 = np.arange(n_S4 + 1)

# Calculate the PMFs for X_S3 and X_S4 using the binomial distribution
pmf_S3 = binom.pmf(x_values_S3, n_S3, p_T)
pmf_S4 = binom.pmf(x_values_S4, n_S4, p_T)

# Plot the PMFs
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.bar(x_values_S3, pmf_S3, align='center', alpha=0.7)
plt.title(f'PMF of X_S3 (Length: {sequence_length_S3})')
plt.xlabel('Number of T occurrences')
plt.ylabel('Probability')
plt.grid(True)

plt.subplot(122)
plt.bar(x_values_S4, pmf_S4, align='center', alpha=0.7)
plt.title(f'PMF of X_S4 (Length: {sequence_length_S4})')
plt.xlabel('Number of T occurrences')
plt.ylabel('Probability')
plt.grid(True)

plt.tight_layout()
plt.show()

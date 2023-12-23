import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

def true_probability(c, lambda_T):
    return 1 - poisson.cdf(c * lambda_T, mu=lambda_T)

def markov_inequality(c, lambda_T):
    return 1/c

def chebyshev_inequality(c, lambda_T):
    return 1/((c-1)**2 * lambda_T)

def chernoff_bound(c, lambda_T):
    exponent = -lambda_T * (c * np.log(c) - c + 1)
    return np.exp(exponent)

def plot_probabilities(c_values, lambda_T):
    true_probs = [true_probability(c, lambda_T) for c in c_values]
    markov_probs = [markov_inequality(c, lambda_T) for c in c_values]
    chebyshev_probs = [chebyshev_inequality(c, lambda_T) for c in c_values]
    chernoff_probs = [chernoff_bound(c, lambda_T) for c in c_values]
    
    # Plotting
    plt.plot(c_values, true_probs, label='True Probability', marker='o')
    plt.plot(c_values, markov_probs, label="Markov's Inequality", marker='o')
    plt.plot(c_values, chebyshev_probs, label="Chebyshev's Inequality", marker='o')
    plt.plot(c_values, chernoff_probs, label="Chernoff Bound", marker='o')

    plt.xlabel('c')
    plt.ylabel('Probability')
    plt.title('Comparison of Probabilities and Bounds')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Set parameters
    lambda_T = 0.001
    c_values = np.linspace(1, 1000, 30)

    # Calculate and plot probabilities
    plot_probabilities(c_values, lambda_T)


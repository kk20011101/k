import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import measurements

def percolation_simulation(p, size, num_simulations):
    results = []

    for _ in range(num_simulations):
        # Create a random grid where each site is open with probability p
        grid = np.random.rand(size, size) < p

        # Label the clusters
        lw, num = measurements.label(grid)

        # Find the labels of the clusters that percolate (span from top to bottom)
        perc_labels = np.intersect1d(lw[0, :], lw[-1, :])

        # Check if any cluster percolates
        percolates = len(perc_labels[perc_labels > 0]) > 0
        results.append(percolates)

    # Calculate the probability of percolation
    percolation_probability = np.mean(results)
    return percolation_probability, results

# Example usage
p = 0.5927
size = 100
num_simulations = 1

percolation_probability, results = percolation_simulation(p, size, num_simulations)

print(f"Percolation probability: {percolation_probability}")

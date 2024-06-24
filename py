import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def create_lattice(n):
    """
    Create an n x n square lattice graph
    """
    G = nx.grid_2d_graph(n, n)
    pos = dict((n, n) for n in G.nodes())
    return G, pos

def bond_percolation(G, p):
    """
    Perform bond percolation on graph G with bond probability p
    """
    H = G.copy()
    for edge in G.edges():
        if np.random.rand() > p:
            H.remove_edge(*edge)
    return H

def plot_lattice(G, pos, title):
    """
    Plot the lattice graph G with given positions pos
    """
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=False, node_size=10, node_color='black', edge_color='blue')
    plt.title(title)
    plt.show()

# Parameters
n = 20  # size of the lattice
p = 0.5  # bond probability

# Create lattice
G, pos = create_lattice(n)

# Perform bond percolation
H = bond_percolation(G, p)

# Plot original lattice
plot_lattice(G, pos, "Original Lattice")

# Plot percolated lattice
plot_lattice(H, pos, "Percolated Lattice (p = {:.2f})".format(p))

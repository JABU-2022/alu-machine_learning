#!/usr/bin/env python3
"""
Absorbing Markov Chain Detection

This script defines a function that determines if a given Markov chain,
represented by its transition matrix, is absorbing.
"""

import numpy as np

def absorbing(P):
    """
    Determines if a Markov chain is absorbing.
    
    Args:
        P: 2D numpy.ndarray of shape (n, n) representing the transition matrix
           P[i, j] is the probability of transitioning from state i to state j
           n is the number of states in the Markov chain
    
    Returns:
        True if the Markov chain is absorbing, False otherwise
    """
    if not isinstance(P, np.ndarray) or len(P.shape) != 2:
        return False
    n, m = P.shape
    if n != m:
        return False

    D = np.diagonal(P)
    if (D == 1).all():
        return True
    if not (D == 1).any():
        return False
    
    absorbing_states = np.where(D == 1)[0]
    if len(absorbing_states) == 0:
        return False

    reachability = np.linalg.matrix_power(P, n)
    for i in range(n):
        if not any(reachability[i, absorbing_states] > 0):
            return False
    
    return True

# Test cases
if __name__ == "__main__":
    test_matrices = [
        np.eye(2),
        np.array([[0.6, 0.4], [0.3, 0.7]]),
        np.array([[0.25, 0.2, 0.25, 0.3], [0.2, 0.3, 0.2, 0.3], [0.25, 0.25, 0.4, 0.1], [0.3, 0.3, 0.1, 0.3]]),
        np.array([[0.8, 0.2, 0, 0, 0], [0.25, 0.75, 0, 0, 0], [0, 0, 0.5, 0.2, 0.3], [0, 0, 0.3, 0.5, .2], [0, 0, 0.2, 0.3, 0.5]]),
        np.array([[1, 0, 0, 0, 0], [0.25, 0.75, 0, 0, 0], [0, 0.1, 0.5, 0.2, 0.2], [0, 0.1, 0.2, 0.5, .2], [0, 0.1, 0.2, 0.2, 0.5]]),
        np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0.5, 0.5], [0, 0.5, 0.5, 0]])
    ]
    
    for matrix in test_matrices:
        print(absorbing(matrix))


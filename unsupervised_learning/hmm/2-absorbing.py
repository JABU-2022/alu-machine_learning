import numpy as np

def absorbing(P):
    """
    Function that determines if a Markov chain is absorbing
    Args:
        P: 2D numpy.ndarray of shape (n, n) representing the transition matrix
           P[i, j]: is the probability of transitioning from state i to state j
           n: the number of states in the Markov chain
    Returns: True if it is absorbing, or False on failure
    """
    if len(P.shape) != 2:
        return False
    n1, n2 = P.shape
    if (n1 != n2) or not isinstance(P, np.ndarray):
        return False
    
    D = np.diagonal(P)
    if (D == 1).all():
        return True
    if not (D == 1).any():
        return False
    
    # Identifying absorbing states
    absorbing_states = np.where(D == 1)[0]
    
    # If there are no absorbing states, return False
    if len(absorbing_states) == 0:
        return False
    
    # Constructing the reachability matrix
    reachability = np.linalg.matrix_power(P, n1)
    
    # Checking if every state can reach an absorbing state
    for i in range(n1):
        if not any(reachability[i, absorbing_states] > 0):
            return False
    
    return True

# Example usage:
P = np.array([
    [0.5, 0.5, 0, 0],
    [0.2, 0.3, 0.5, 0],
    [0, 0, 1, 0],
    [0, 0, 0.2, 0.8]
])

print(absorbing(P))  # Output should be True


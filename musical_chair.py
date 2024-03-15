def find_winning_child(N, K):
    # Initialize an array to represent the children
    children = list(range(1, N + 1))
    # Initialize the index pointing to the starting child
    index = 0
    
    # Iterate until only one child remains
    while len(children) > 1:
        # Calculate the index of the child to be removed
        remove_index = (index + K - 1) % len(children)
        # Remove the child from the list
        del children[remove_index]
        # Update the index for the next round
        index = remove_index % len(children)
    
    # Return the winning child
    return children[0]

# Example usage:
N = 14
K = 20
print("The winning child is:", find_winning_child(N, K))

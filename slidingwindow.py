def sliding_window(sequence, window_size):
    if window_size > len(sequence):
        raise ValueError("Window size cannot be larger than the sequence length.")   
    for i in range(len(sequence) - window_size + 1):
        yield sequence[i:i+window_size]
sequence = [1, 3, 5, 2, 7, 4, 8, 9, 5, 3, 5 , 7, 9, 3, 2 ,0]
window_size = int(input("Enter the window size dear!!!"))
for window in sliding_window(sequence, window_size):
    print(window)
def sliding_window(sequence,window_size):
    if window_size > len(sequence):
        raise ValueError("window size cannot be larger than the sequemce length.")
    for i in range (len(sequence) - window_size+1):
        yield sequence[i:i+window_size]
sequence = [1,3,5,6,2,7,8,5,9,0,2,3,9]
window_size = int(input("enter the window size"))
for window in sliding_window( sequence , window_size):
    print(window)        
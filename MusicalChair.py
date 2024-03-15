def last_win(N, k):
    arr = list(range(1, N + 1))
    if len(arr) > 1:
        j = 0
        while len(arr) > 1:
            j = (j + k - 1) % len(arr)
            arr.pop(j)
        print("Last person  ", arr[0])
    else:
        print("only one left")
last_win(14, 20)
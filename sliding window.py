if __name__ == '__main__':
    arr: list = [1, 3, 5, 2, 7, 4, 8, 9, 5, 3, 5, 7, 9, 3, 2, 0]
    k: int = int(input('enter k '))
    var_sum: int = 0  # initialize sum as zero

    # found a sum of the first three elements
    for i in range(k):
        var_sum = var_sum + arr[i]

    window: int = var_sum  # initialize a window as sum
    for i in range(len(arr) - k):
        if window > var_sum:
            var_sum = window

        window = window - arr[i] + arr[i + k]

    print(var_sum)
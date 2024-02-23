from collections import deque

N = 9
K = 3
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]

if K > N:
    print("Invalid input.")
else:
    result = []  # To store the maximum values of each subarray
    dq = deque()

    # Process the first window
    for i in range(K):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)

    # Process the rest of the array
    for i in range(K, N):
        result.append(arr[dq[0]])

        # Remove elements outside the current window
        while dq and dq[0] <= i - K:
            dq.popleft()

        # Remove elements smaller than the current element
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    # Append the maximum value of the last subarray
    result.append(arr[dq[0]])

    print("Output:", result)

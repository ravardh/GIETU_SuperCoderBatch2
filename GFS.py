class Solution:
    def max_of_subarrays(self, arr, n, k):
        res = []
        if arr is None or k <= 0:
            return res
        q = deque()
        for i in range(n):
            while q and q[0] <= i - k:
                q.popleft()
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(arr[q[0]])
        return res
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        mx = [[0] * m for _ in range(n)]
        mn = [[0] * m for _ in range(n)]

        for i, x in enumerate(nums):
            mx[i][0] = x
            mn[i][0] = x

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            length = 1 << j

            for i in range(n - length + 1):
                mx[i][j] = max(mx[i][j - 1], mx[i + half][j - 1])
                mn[i][j] = min(mn[i][j - 1], mn[i + half][j - 1])

            j += 1

        def value(l: int, r: int) -> int:
            p = lg[r - l + 1]
            mxv = max(mx[l][p], mx[r - (1 << p) + 1][p])
            mnv = min(mn[l][p], mn[r - (1 << p) + 1][p])
            return mxv - mnv

        pq = []

        for l in range(n):
            heappush(pq, (-value(l, n - 1), l, n - 1))

        ans = 0

        for _ in range(k):
            v, l, r = heappop(pq)
            ans -= v

            if r > l:
                heappush(pq, (-value(l, r - 1), l, r - 1))

        return ans

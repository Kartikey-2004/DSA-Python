from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]),
            )
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]),
            )
        ans = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            dist = id2 - id1
            ans = max(ans, (h1 + h2 + dist) // 2)
        return ans

from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        max_depth = 0

        def dfs(u, parent, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            for v in g[u]:
                if v != parent:
                    dfs(v, u, depth + 1)

        dfs(1, 0, 0)

        return pow(2, max_depth - 1, MOD)

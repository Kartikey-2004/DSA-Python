from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = n.bit_length()

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [(1, 0)]
        while stack:
            node, parent = stack.pop()
            up[0][node] = parent

            for nei in graph[node]:
                if nei != parent:
                    depth[nei] = depth[node] + 1
                    stack.append((nei, node))

        for k in range(1, LOG):
            for v in range(1, n + 1):
                up[k][v] = up[k - 1][up[k - 1][v]]

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)
            length = depth[u] + depth[v] - 2 * depth[ancestor]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow2[length - 1])

        return ans

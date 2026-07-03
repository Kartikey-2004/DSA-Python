from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        heap = [(-dist[0][0], 0, 0)]
        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        while heap:
            safe, x, y = heappop(heap)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            if safe < best[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    new_safe = min(safe, dist[nx][ny])

                    if new_safe > best[nx][ny]:
                        best[nx][ny] = new_safe
                        heappush(heap, (-new_safe, nx, ny))

        return 0

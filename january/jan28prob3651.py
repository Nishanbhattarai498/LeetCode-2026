from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[t][i][j] = min cost to reach (i,j) using t teleports
        dist = [[[INF] * n for _ in range(m)] for _ in range(k + 1)]
        dist[0][0][0] = 0

        # All cells sorted by value (for teleport optimization)
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        # Pointer per teleport layer
        ptr = [0] * (k + 1)

        # Min-heap: (cost, i, j, teleports_used)
        pq = [(0, 0, 0, 0)]

        while pq:
            cost, i, j, t = heapq.heappop(pq)

            if cost != dist[t][i][j]:
                continue

            # Normal moves (right & down)
            if j + 1 < n:
                nc = cost + grid[i][j + 1]
                if nc < dist[t][i][j + 1]:
                    dist[t][i][j + 1] = nc
                    heapq.heappush(pq, (nc, i, j + 1, t))

            if i + 1 < m:
                nc = cost + grid[i + 1][j]
                if nc < dist[t][i + 1][j]:
                    dist[t][i + 1][j] = nc
                    heapq.heappush(pq, (nc, i + 1, j, t))

            # Teleportation
            if t < k:
                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[i][j]:
                    _, x, y = cells[ptr[t]]
                    if cost < dist[t + 1][x][y]:
                        dist[t + 1][x][y] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    ptr[t] += 1

        # Minimum cost to reach bottom-right using <= k teleports
        ans = min(dist[t][m - 1][n - 1] for t in range(k + 1))
        return -1 if ans == INF else ans





import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        # Build graph: normal + reversed edges
        for u, v, w in edges:
            graph[u].append((v, w))        # original direction
            graph[v].append((u, 2 * w))    # reversed using switch

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]

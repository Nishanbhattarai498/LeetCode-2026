from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        INF = 10**18  # A very large number for impossible paths
        
        # Step 1: Initialize the distance matrix for 26 letters
        dist = [[INF]*26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0  # Cost to convert a letter to itself is 0
        
        # Step 2: Add the given transformation edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)  # If multiple edges, take minimum cost
        
        # Step 3: Floyd-Warshall to compute all-pairs minimum cost
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Step 4: Calculate total cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue  # No cost if characters are already same
            s_idx = ord(s_char) - ord('a')
            t_idx = ord(t_char) - ord('a')
            if dist[s_idx][t_idx] == INF:
                return -1  # Impossible to convert
            total_cost += dist[s_idx][t_idx]
        
        return total_cost


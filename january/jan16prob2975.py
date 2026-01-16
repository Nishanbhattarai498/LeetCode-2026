class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        # Compute all possible distances between horizontal fences
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # Compute all possible distances between vertical fences
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find the maximum common side length
        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD

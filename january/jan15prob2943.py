from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def longest_consecutive(bars: List[int]) -> int:
            bars.sort()
            longest = curr = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            return longest
        
        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)
        
        side = min(max_h + 1, max_v + 1)
        return side * side


from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * (m + 1) for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
                col_prefix[c][r + 1] = col_prefix[c][r] + grid[r][c]
        
        # Helper functions to get sums in O(1)
        def get_row_sum(r, c1, c2):
            return row_prefix[r][c2 + 1] - row_prefix[r][c1]
        
        def get_col_sum(c, r1, r2):
            return col_prefix[c][r2 + 1] - col_prefix[c][r1]
        
        # Check if a square starting at (r, c) with size k is magic
        def is_magic(r, c, k):
            # Calculate target sum from first row
            target = get_row_sum(r, c, c + k - 1)
            
            # Check all rows
            for i in range(r, r + k):
                if get_row_sum(i, c, c + k - 1) != target:
                    return False
            
            # Check all columns
            for j in range(c, c + k):
                if get_col_sum(j, r, r + k - 1) != target:
                    return False
            
            # Check main diagonal
            diag_sum = 0
            for d in range(k):
                diag_sum += grid[r + d][c + d]
            if diag_sum != target:
                return False
            
            # Check anti-diagonal
            anti_diag_sum = 0
            for d in range(k):
                anti_diag_sum += grid[r + d][c + k - 1 - d]
            if anti_diag_sum != target:
                return False
            
            return True
        
        # Try all possible sizes from largest to smallest
        max_size = min(m, n)
        for k in range(max_size, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        
        return 1  # Every 1x1 grid is trivially magic
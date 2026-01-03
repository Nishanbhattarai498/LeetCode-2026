class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # For the first row
        aba = 6  # patterns like A B A
        abc = 6  # patterns like A B C
        
        for _ in range(2, n + 1):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD
            
            aba, abc = new_aba, new_abc
        
        return (aba + abc) % MOD

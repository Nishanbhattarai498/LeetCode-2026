from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # dp[i][j] = max dot product using first i elements of nums1 and first j elements of nums2
        dp = [[float('-inf')] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # Option 1: take nums1[i-1] and nums2[j-1] together
                take_both = nums1[i-1] * nums2[j-1] + max(0, dp[i-1][j-1])
                # Option 2: skip nums1[i-1]
                skip_nums1 = dp[i-1][j]
                # Option 3: skip nums2[j-1]
                skip_nums2 = dp[i][j-1]
                
                # Maximum of all options
                dp[i][j] = max(take_both, skip_nums1, skip_nums2)
        
        return dp[n][m]

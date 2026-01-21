
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
                continue
            n = num + 1
            k = 0
            while n % 2 == 0:
                k += 1
                n //= 2
            ans.append(num - (1 << (k - 1)))
        return ans
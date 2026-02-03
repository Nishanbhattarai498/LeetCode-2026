class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # 1️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False

        # 2️⃣ strictly decreasing
        p = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == p:
            return False

        # 3️⃣ strictly increasing again
        q = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == q:
            return False

        return i == n - 1

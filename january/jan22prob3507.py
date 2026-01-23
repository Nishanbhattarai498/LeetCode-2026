class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        
        operations = 0
        
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            index = 0
            
            # Find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    index = i
            
            # Replace the selected pair with their sum
            nums = nums[:index] + [min_sum] + nums[index + 2:]
            operations += 1
        
        return operations
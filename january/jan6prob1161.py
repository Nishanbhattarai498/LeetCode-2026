from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])  # queue for BFS
        level = 1          # current level
        max_sum = float('-inf')  # maximum sum found so far
        answer = 1         # level with max sum
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # update max_sum and answer if current level sum is greater
            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
            
            level += 1  # move to next level
        
        return answer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # First DFS to calculate total sum of the tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        self.max_prod = 0
        
        # Second DFS to calculate subtree sums and max product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            sub_sum = node.val + left + right
            
            # product if edge above this subtree is removed
            self.max_prod = max(self.max_prod, sub_sum * (total - sub_sum))
            
            return sub_sum
        
        dfs(root)
        return self.max_prod % MOD

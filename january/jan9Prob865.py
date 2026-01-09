# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Helper function: returns (subtree_root, depth)
        def dfs(node: Optional[TreeNode]) -> tuple[Optional[TreeNode], int]:
            if not node:
                return (None, 0)
            
            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)
            
            if left_depth > right_depth:
                return (left_subtree, left_depth + 1)
            elif right_depth > left_depth:
                return (right_subtree, right_depth + 1)
            else:
                # If left and right depths are equal, current node is the LCA
                return (node, left_depth + 1)
        
        subtree_root, _ = dfs(root)
        return subtree_root

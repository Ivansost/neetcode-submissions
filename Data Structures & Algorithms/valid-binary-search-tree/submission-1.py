# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, low, high):
            if node is None:
                return True

            if not (low < node.val < high):
                return False

            left_ok = check(node.left, low, node.val)
            right_ok = check(node.right, node.val, high)

            return left_ok and right_ok

        return check(root, float('-inf'), float('inf'))
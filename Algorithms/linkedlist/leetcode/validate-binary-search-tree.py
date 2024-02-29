# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def sol_rec(root,minimum, maximum):
      if not root:
        return True
      if minimum and root.val <= minimum.val:
        return False
      if maximum and root.val >= maximum.val:
        return False

      return sol_rec(root.left, minimum, root) and sol_rec(root.right, root, maximum)

    return sol_rec(root, None, None)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sol_rec(root):
            global ans
            if (root is None) :
                return 
            else:
                if root.val>=low and root.val<=high:
                    ans+=root.val
                if root.val >low:
                    sol_rec(root.left)
                if root.val <high:
                    sol_rec(root.right)
        global ans
        ans=0
        sol_rec(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sol_rec(ptr1,ptr2):
            if not ptr1 and ptr2 or not ptr2 and ptr1:
                return False
            if ptr1 and ptr2 and ptr1.val!=ptr2.val:
                return False
            if ptr1 and ptr2 and not sol_rec(ptr1.left,ptr2.left):
                return False
            if ptr1 and ptr2 and not sol_rec(ptr1.right,ptr2.right):
                return False
            return True
        ans=sol_rec(p,q)
        return ans
            
        
        
        
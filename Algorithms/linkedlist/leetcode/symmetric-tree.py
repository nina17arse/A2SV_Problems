# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sol_rec(ptr1,ptr2):
            if not ptr1 and ptr2 or not ptr2 and ptr1:
                return False
                
            if ptr1 and ptr2 and ptr1.val!=ptr2.val:
                return False
                
            if ptr1 and ptr2 and not sol_rec(ptr1.left,ptr2.right):
                return False
                
            if ptr1 and ptr2 and not sol_rec(ptr1.right,ptr2.left):
                return False
                
            return True
        
        ans=sol_rec(root,root)
        
        return ans

        
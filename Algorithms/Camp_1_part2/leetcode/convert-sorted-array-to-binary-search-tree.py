# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sol_rec(l,r):
            if l>r:
                return None
            avg=(l+r)//2
            l=sol_rec(l,avg-1)
            r=sol_rec(avg+1,r)
            return TreeNode(nums[avg],l,r)

        
        return sol_rec(0,len(nums)-1)
        
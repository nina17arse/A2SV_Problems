# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol_rec(self,curr, minv, maxv,ans):
            if curr:
                minv = min(minv, curr.val)
                maxv = max(maxv, curr.val)
                ans.append(abs(minv-maxv))

                self.sol_rec(curr.left, minv, maxv,ans)
                self.sol_rec(curr.right, minv, maxv,ans)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=[]
        self.sol_rec(root, root.val, root.val,ans)
        return max(ans)
        

                
        
        
        
        
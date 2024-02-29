# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol_rec(self,node,ans):
            if node is None:
                return None
            self.sol_rec(node.left,ans)
            ans.append(node.val)
            self.sol_rec(node.right,ans)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        self.sol_rec(root,ans)
        return ans[k-1]
    
        
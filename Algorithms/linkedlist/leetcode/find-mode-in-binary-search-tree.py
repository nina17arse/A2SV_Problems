# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sol_rec(self,node,dic):
        if node is None:
            return None
        if node:
            dic[node.val]=dic.get(node.val,0) + 1

        if node.left:
            self.sol_rec(node.left,dic)
        if node.right:
            self.sol_rec(node.right,dic)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        dic={}
        self.sol_rec(root,dic)
        maxOccur=max(dic.values())
        for k,v in dic.items():
            if v==maxOccur:
                ans.append(k)
        return ans
        
        
        
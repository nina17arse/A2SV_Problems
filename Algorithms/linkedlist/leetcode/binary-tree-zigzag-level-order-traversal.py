# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
            
            
            

        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        dic=defaultdict(list)

        def sol_rec(node,idx):
            if node is None:
                return None
            dic[idx].append(node.val)
            sol_rec(node.left,idx+1)
            sol_rec(node.right,idx+1)
            

   
        sol_rec(root,0)

        maxNum=max(dic.keys())
        for i in range(0,maxNum+1):
            if i%2==0:
                ans.append(dic[i])
            else:
                ans.append(reversed(dic[i]))
        return ans

        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if root is None:
                return

            queue = deque()
            queue.appendleft([root,1])

            width=1
            while queue:
                for i in range(len(queue)):
                    node=queue.pop()
                    if node[0].left:
                        queue.appendleft([node[0].left,2*node[1] - 1])
                    if node[0].right:
                        queue.appendleft([node[0].right,2*node[1]])
                if len(queue)==0:
                    break
                width=max((queue[0][1]-queue[-1][1]) + 1, width)
            return width
        return bfs(root)
                
            

        
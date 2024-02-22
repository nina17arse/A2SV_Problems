class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        # newList=None
        newList=list(map(str,path.split("/")))
        print(newList)
        for chx in newList:
            if chx=="." or not chx:
                continue
            elif chx=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(chx)
        # print(stack)
        
        return "/" + "/".join(stack)
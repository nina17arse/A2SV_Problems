class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={
            '(': ')',
            '{': '}',
            '[': ']',
         }
        for x in s:
            if x in dic:
                stack.append(x)
            elif len(stack)==0 or x != dic[stack.pop()]:
                return False
        
        return len(stack)==0

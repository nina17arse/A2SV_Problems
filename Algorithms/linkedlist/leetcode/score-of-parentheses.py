class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        x=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append("(")
            elif s[i]==")":
                if stack[-1]=="(":
                    stack.pop()
                    x=1
                elif stack[-1]!="(":
                    x=(int(stack.pop()))
                    if stack and stack[-1]=="(":
                        stack.pop()
                        x*=2
                while stack and  stack[-1]!="(" :
                    x += int(stack.pop())
                stack.append(x)       
        
        return (stack.pop())
                



        
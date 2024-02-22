class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=["+","-","*","/"]
        ans=""
        for i in range(len(tokens)):
            if tokens[i]=="/":
                a=stack.pop()
                b=stack.pop()
                if a*b>0:
                    stack.append(math.floor(b/a))
                else:
                    stack.append(math.ceil(b/a))
            
            elif tokens[i]=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
                
            elif tokens[i]=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif tokens[i]=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif tokens[i] not in op:
                stack.append(int(tokens[i]))
        
        return (stack[0])
        
        
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for chr in s:
            if chr!="*":
                stack.append(chr)
            elif chr=="*":
                stack.pop()
        result = ''.join(str(element) for element in stack)
        return result

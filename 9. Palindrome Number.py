class Solution:
    def isPalindrome(self, x: int) -> bool:
        y= str(x)
        reversed_y=y[::-1]
        if reversed_y==y:
            return True
        else:
            return False
        

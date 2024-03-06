# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<=right:
            x=(left+right)//2
            if guess(x)==-1:
                right=x-1
            elif guess(x)==1:
                left=x+1
            elif guess(x)==0:
                return x
        return x

            
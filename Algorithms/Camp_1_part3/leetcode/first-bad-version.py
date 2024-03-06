# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int,key=lambda x: True) -> int:
        left=1
        right=n
        ff=0
        while left<=right:
            mid= (left + right) //2
            if isBadVersion(mid):
                ff=mid
                right=mid-1
            else:
                left=mid+1

        return right+1


                

        
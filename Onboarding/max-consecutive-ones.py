class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=None
        r=0
        ans=0
        while r < len(nums):
            if nums[r]==1 and l==None:
                l=r
            if nums[r]==0:
                if l!=None:
                    ans=max(ans,r-l)
                l=None
            r+=1
        if l!=None:
            ans=max(ans,r-l) 
        return ans


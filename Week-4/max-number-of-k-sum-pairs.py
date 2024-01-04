class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        count=0
        dic={}
        while l < r and len(nums)>0:
            if nums[l]+nums[r]<k:
                l+=1
            elif nums[l]+nums[r]>k:
                r-=1
            elif nums[l]+nums[r]==k:

                count+=1
                l+=1
                r-=1
        return count

class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstele=nums[0]
        lastele=nums[-1]
        left,right=0,len(nums)-1
        minN=float("inf")
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return min(nums)
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<minN:
                minN=nums[mid]
            if nums[mid] < nums[right]:
                right=mid-1
            else:
                left=mid+1

        return minN
                

        




            
            
        
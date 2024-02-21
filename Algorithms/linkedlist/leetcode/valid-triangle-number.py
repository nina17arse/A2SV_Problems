class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        count=0
        
        for k in range(2,len(nums)):
            l=0
            r=k-1
            while r !=l:
                if nums[l]+nums[r]>nums[k]:
                    count+=r-l
                    r-=1
                else:
                    l+=1
                    

        return count

            




        
class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sol=[]
        for i in range(0,len(nums)):
            v=0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    v+=1
            sol.append(v)
         
        return sol

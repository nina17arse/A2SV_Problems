class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)):
            
            if target == nums[i]:
                res.append(i)
        return res

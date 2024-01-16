class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pSum=[nums[0]]
        for i in range(1,len(nums)):
            pSum.append(nums[i]+pSum[i-1])
        return pSum
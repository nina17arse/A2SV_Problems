class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        currSum,res=0,0
        prefixSums={0:1}
        for n in nums:
            currSum+=n
            difference=currSum - goal
            res+=prefixSums.get(difference,0)
            prefixSums[currSum]=prefixSums.get(currSum,0) + 1
        
        return res
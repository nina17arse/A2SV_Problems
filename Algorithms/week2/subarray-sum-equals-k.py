class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum,res=0,0
        prefixSums={0:1}
        for n in nums:
            currSum+=n
            difference=currSum - k
            res+=prefixSums.get(difference,0)
            prefixSums[currSum]=1+prefixSums.get(currSum,0)
        
        return res




        
        
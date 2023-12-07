class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            dic[num]=True
        for x in range(len(nums)+ 1):
            if x not in dic:
                return x

        
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res=[]
        left=0
        right=sum(nums)
        for i,num in enumerate(nums):
            left_sum=num*i - left
            right_sum=right-num*(len(nums)-i)

            tot=left_sum+right_sum
            res.append(tot)
            left+=num
            right-=num
        return res

        
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su=sum(nums[:k])
        windSum=su
        for i in range(1,len(nums)-k+1):
            windSum=windSum - nums[i-1] + nums[i+k-1]
            su=max(su,windSum)
        return su/k


        
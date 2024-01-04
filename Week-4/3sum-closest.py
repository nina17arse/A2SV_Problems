class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans=float("inf")
        res=0
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                sumN = nums[i] + nums[l] + nums[r]
                if abs(sumN - target) < ans:
                    ans=abs(sumN-target)
                    res = nums[i] + nums[l] + nums[r]
                   
                if sumN < target:
                    l+=1
                else:
                    r-=1
        return res

            
        
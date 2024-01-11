class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # l=0
        # r=l+1
        # window=[]

        # while r<len(nums):
        #     if nums[l]!=nums[r]:
        #         sze=r-l+1
        #         window=nums[l:r]
        #         r+=1
        #     else:
        #         l+=1
        #         r=l+1
        # return sum(window)
        ans = 0
        score = 0
        seen = set()

        l = 0
        for r, num in enumerate(nums):
            while num in seen:
                score -= nums[l]
                seen.remove(nums[l])
                l += 1
            seen.add(nums[r])
            score += nums[r]
            ans = max(ans, score)

        return ans

        
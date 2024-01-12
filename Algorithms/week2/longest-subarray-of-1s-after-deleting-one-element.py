class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        count_zero = 0

        for num in nums:
            if num == 0:
                count_zero += 1
            if count_zero > 1:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1

        return len(nums) - l - 1

        
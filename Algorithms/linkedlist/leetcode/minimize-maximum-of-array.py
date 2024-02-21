class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        max_num = nums[0]
        prefix_sum = nums[0]

        for idx in range(1, len(nums)):
            curr = nums[idx]
            prefix_sum += curr
            if curr > max_num:
                max_num=max(max_num, math.ceil(prefix_sum/(idx+1)))
        return max_num
                        

        
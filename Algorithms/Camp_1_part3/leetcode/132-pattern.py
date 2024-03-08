class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        prevMax = float('-inf')
        n = len(nums) - 1
        for i in range(n,-1,-1):
            num = nums[i]
            if num < prevMax: return True

            while stack and stack[-1] < num:
                prevMax = stack.pop()
            stack.append(num)
        
        return False
        
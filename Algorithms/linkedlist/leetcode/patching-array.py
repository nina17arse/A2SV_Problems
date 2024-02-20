class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    missing_num=1 
    idx=0
    patches = 0
    while missing_num <= n:
        if idx < len(nums) and nums[idx] <= missing_num:
            missing_num += nums[idx]
            idx += 1
        else:
            missing_num *= 2
            patches += 1
    return patches

        
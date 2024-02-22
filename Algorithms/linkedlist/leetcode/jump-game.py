class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hop=0
        for i in range(len(nums)):
            if i > hop:
                return False
            
            hop=max(hop,i+nums[i])
        
        return True
        

        
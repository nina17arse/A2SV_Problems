class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            x=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(x)
            ans.extend(perms)
            nums.append(x)
        return ans
    
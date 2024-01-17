class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        pref_prod=[1]*length
        for i in range(1,length):
            pref_prod[i]=pref_prod[i-1]*nums[i-1]
        right=nums[-1]
        for i in range(length-2,-1,-1):
            pref_prod[i]*=right
            right*=nums[i]

        return pref_prod

        
        
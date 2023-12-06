class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        maxCount=n/3
        res=[]
        check={}
        # if n < 3:
        #     res=[x for x in nums if ]
        #     return res
        # else:
        for y in nums:
            check[y]=nums.count(y)
        for key,value in check.items():
            if value > maxCount:
                res.append(key)
        return res



        
            


        
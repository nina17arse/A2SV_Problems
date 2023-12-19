class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # ans=[]
        # l=0
        # r=1
        # while r < len(nums):
        #     if nums[l] == nums[r] and l*r % k ==0:
        #         ans.append((nums[l],nums[r]))
                
        #         l+=1
        #         r+=1
        #     else:
        #         l+=1
        #         r+=1
        # return len(ans)
        count=0
        for i in range(0,len(nums)):
            for u in range(i+1,len(nums)):
                if nums[i]==nums[u] and (i*u)%k==0:
                    count+=1
        return count
        
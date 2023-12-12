class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        evenNums=[p for p in nums if p%2==0]
        evenSum=sum(evenNums)
        for key,value in queries:
            if nums[value]%2==0:
                evenSum-=nums[value]
            nums[value]+=key
            if nums[value]%2==0:
                evenSum+=nums[value]
            ans.append(evenSum)
        return ans

            
        
       
        
                
        
        



        
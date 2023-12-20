class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[]
        ones=nums.count(1)
        ans.append(ones)
        s=0
        zeros=0
        lOnes=0
        res=[]
        
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            else:
                lOnes+=1
            rOnes=ones-lOnes
            s=zeros+rOnes
            ans.append(s)
        maxSum=max(ans)
        for x in range(0,len(ans)):
            if ans[x] == maxSum:
                res.append(x)
        return res



        
        # rOnes=s-ones
        # print(rOnes)




        # return maxSum

            

        
            

        
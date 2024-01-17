class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        chrCount=Counter(s)
        toBeRep={}
        l=0
        r=0
        wind=s[l]
        countDic=Counter()
        ans=float("inf")
        for k,v in chrCount.items():
            if v > n//4:
                toBeRep[k]=v-n//4
        # print(toBeRep)
        def check_valid():
            if not toBeRep:
                return 0
            for k in toBeRep:
                if countDic[k]<toBeRep[k]:
                    return False
            return True
        while r < n:
            countDic[s[r]]+=1
            if check_valid():
                # print(l,r,countDic)
                
                while check_valid():
                    countDic[s[l]]-=1
                    ans=min(ans,r-l+1)
                    l+=1
            r+=1
        
        return ans if ans < float("inf") else 0

            
        
        
        

       
        
                   
            
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1st Approach
        ws=0
        d={}
        freq=0
        maxlen=0
        for we in range(len(s)):
            c=s[we]
            d[c]=d.get(c,0)+1
            freq=max(freq,d[c])
            if we-ws+1-freq>k:
                leftchar=s[ws]
                d[leftchar]-=1
                if d[leftchar]==0:
                    del d[leftchar]
                ws+=1
            maxlen=max(maxlen,we-ws+1)
        return maxlen
        
        
        
        
        # 2nd Approach Out of Index
        # op=k
        # strCount={}
        # for t in s:
        #     if t not in strCount:
        #         strCount[t]=1
        #     else:
        #         strCount[t]=strCount.get(strCount[t],1) + 1
        # maxTimes=max(strCount.values())
        # if maxTimes==0:
        #     return 2
        # else:
        #     for k,v in strCount.items():
        #         if v == maxTimes:
        #             maxOccur=k
            
        #     left=0
        #     right=1
        #     wind=s[left]
        #     ans=0
        #     while right<len(s)-1 or op > 0:
        #         if s[right]==maxOccur:
        #             ans+=1
        #             right+=1
        #         else:
        #             ans+=1
        #             op-=1
        #             right+=1
        #     return ans

                
            
            
            
        
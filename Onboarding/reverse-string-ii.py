class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        if len(s)<=1 or k <= 1:
            ans+=s
            return ans
        else:
            for i in range(0, len(s),2*k):
                temp=s[i:i+k]
                tempS=temp[::-1]
                ans += tempS + s[i+k:i+2*k]
            return ans
            
        
        

            
        
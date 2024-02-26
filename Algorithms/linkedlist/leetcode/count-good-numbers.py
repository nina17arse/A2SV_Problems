class Solution:
    @cache
    def countGoodNumbers(self, n: int) -> int:
        modNum=(10**9)+7
        if n%2 == 0:
            evenPart = n //2
        else:
            evenPart = 1+ n //2
        oddPart = n //2
        def powF(fiveOrFour,n):
            modNum=(10**9)+7
            if n==1:
                return fiveOrFour
            elif n==0:
                return 1

            if n%2==0:
                res=powF(fiveOrFour,n//2)
                ans=(res**2)% modNum
                return ans
            else:
                res=powF(fiveOrFour,n//2)
                ans=((res**2)*(fiveOrFour)) % modNum
                return ans

        return ((powF(4,oddPart) if powF(4,oddPart) else 1) * (powF(5,evenPart))) % modNum

            
            
            
            
        


        
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def sol_rec(x:float,n:int):
            if x==0: 
                return 0
            if n==0: 
                return 1
            res=sol_rec(x,n//2)
            res=res*res
            return x*res if n%2 else res
        res=sol_rec(x,abs(n))
        return res if n>=0 else 1/res

        

        
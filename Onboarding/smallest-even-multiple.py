class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res=inf
        if n % 2 == 0:
            res=n
            return res
        else:
            res=min(res,(n*2))
            return res



        
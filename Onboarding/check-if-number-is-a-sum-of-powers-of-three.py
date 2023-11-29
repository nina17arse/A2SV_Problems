import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base = 3
        exponent=math.log(n,base)
        exp_sum=0
        for x in range(int(exponent),-1,-1):
            if (base**x) + exp_sum <= n:
                exp_sum+=(base**x)
        return exp_sum==n
        
        
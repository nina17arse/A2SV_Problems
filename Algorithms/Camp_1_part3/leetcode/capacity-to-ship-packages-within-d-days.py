class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def sol(mid):
            curr = 0
            day = 0
            for i in range(n):
                curr += weights[i]
                if curr > mid:
                    curr = weights[i]
                    day += 1
            return (day + (1 if curr else 0) > days)
        minW=max(weights)
        maxW=sum(weights)
        ans=0
        while minW<=maxW:
            mid=(minW+maxW)//2
            if sol(mid):
                minW=mid+1
            else:
                maxW=mid-1
                ans=mid
        return ans
        

        
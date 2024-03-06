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
            
        low = max(weights)
        high=sum(weights) 
        ans = high
        while low<=high:
            m = low + ((high-low)//2)
            if sol(m):
                low = m+1
            else:
                high = m-1
                ans = m
        return ans












# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         minW=min(weights)
#         maxW=sum(weights)
#         while minW<=maxW:
#             mid=(minW+maxW)//2
#             if mid > days:
#                 minW=mid+1
#             else:
#                 maxW=mid-1
#         return mid//

        
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value=max(candies)
        res=[]
        for x in candies:
            res.append(x + extraCandies >= max_value)
        return res
        
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        t1=float("inf")
        t2=float("inf")
        for x in nums:
            if x > t2:
                return True
            elif x <= t1:
                t1=min(t1,x)
            elif x <= t2:
                t2=min(t2,x)
        return False

                
            




        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        k_sum = (sum(piles) + h-1) // h  
        
        low, high = k_sum, k_max + 1
        while low < high:
            k = (low+high) // 2
            time = sum((p + k-1) // k for p in piles) 
            if time <= h:
                high = k
            else: 
                low = k + 1
        return low
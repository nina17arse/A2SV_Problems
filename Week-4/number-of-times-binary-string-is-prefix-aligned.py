class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flipped_idx = 0 

        for i, f in enumerate(flips, start=1):
            max_flipped_idx = max(max_flipped_idx, f)
            
            if max_flipped_idx == i: 
                count += 1

        return count
                
            



        
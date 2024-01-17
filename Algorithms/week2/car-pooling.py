class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeLine=defaultdict(int)
        change=0
        for passengers,start,end in trips:
            timeLine[start]+=passengers
            timeLine[end]-=passengers
        for i in sorted(timeLine.keys()):
            change+=timeLine[i]
            if change>capacity:
                return False
        return True


        
        
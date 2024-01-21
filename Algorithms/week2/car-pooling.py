class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeLine=defaultdict(int)
        ch=0
        for passengers,start,end in trips:
            timeLine[start]+=passengers
            timeLine[end]-=passengers
        for i in sorted(timeLine.keys()):
            ch+=timeLine[i]
            if ch>capacity:
                return False
        return True


        
        
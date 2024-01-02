class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        checkpoints = []
        ans = []
        for x in range(len(points)):
            val = points[x][0]**2 + points[x][1]**2
            checkpoints.append((val, tuple(points[x])))

        checksorted = sorted(checkpoints)
        
        for x in range(k):
            ans.append(list(checksorted[x][1]))

        
        return ans
        
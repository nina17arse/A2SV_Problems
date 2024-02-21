class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        #print(points)
        last_point=(points[0][1])
        count=0
        for i in points:
            if i[0]>last_point:
                count+=1
                last_point=i[1]
            last_point=min(i[1],last_point)
        #print(count)
        return count+1

            
        

        
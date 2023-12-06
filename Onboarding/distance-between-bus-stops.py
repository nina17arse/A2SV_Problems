class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        #Initalize Maximum and Minimum Points
        minimumPoint=min(start,destination)
        maximumPoint=max(start,destination)
        #Calculate the distances
        forwardSum=sum(distance[minimumPoint:maximumPoint])
        backwardSum=(sum(distance[:minimumPoint]) + sum(distance[maximumPoint:]))
        #Calculate the minimum of Two
        res=min(forwardSum,backwardSum)
        return res
        
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        stepCount = 0
        current_water = capacity
        n = len(plants)
        for i in range(n):
            if plants[i] > current_water:
                stepCount += 2*i 
                current_water = capacity
            current_water -= plants[i]
            stepCount += 1
        return stepCount

            
            

            

            
        
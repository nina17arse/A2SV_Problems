class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size=len(names)
        for i in range(size):
            for x in range(size-i-1):
                if heights[x] < heights[x+1]:
                    names[x],names[x+1]=names[x+1],names[x]
                    heights[x],heights[x+1]=heights[x+1],heights[x]
        return names
        
        
        
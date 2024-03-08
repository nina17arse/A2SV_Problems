class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        r=[0]*n
        c=[0]*n
        for x in range(n):
            for y in range(n):
                r[x]=max(r[x],grid[x][y])
                c[y]=max(c[y],grid[x][y])
        total=0
        for x in range(n):
            for y in range(n):
                total+=max(min(r[x],c[y])-grid[x][y],0)
        return total

        
        
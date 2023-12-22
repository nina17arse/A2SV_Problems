class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for c in range(i+1,col):
                matrix[i][c],matrix[c][i]=matrix[c][i],matrix[i][c]
        for r in matrix:
            for u in range(row//2):
             r[u], r[row-1-u]=r[row-1-u],r[u]  
        
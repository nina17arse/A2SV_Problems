class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_diagonal_sum = 0
        secondary_diagonal_sum = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    primary_diagonal_sum += mat[i][j]
                if i + j == n - 1 and i != j:
                    secondary_diagonal_sum += mat[i][j]
        return primary_diagonal_sum + secondary_diagonal_sum
            # value=max(value,lDic[i+x]+rDic[i-x]-mat[i][x])
    # print(value)

        
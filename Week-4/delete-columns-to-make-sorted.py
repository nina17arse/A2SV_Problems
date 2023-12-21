class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row, col = len(strs), len(strs[0])
        count = 0

        for i in range(col):
            for j in range(row):
                if (j+1) < row and strs[j][i] > strs[j + 1][i]:
                    count += 1
                    break

        return count
        
        

        



        
        
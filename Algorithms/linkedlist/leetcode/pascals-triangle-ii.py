class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        else:
            previous_row=self.getRow(rowIndex-1)
            curr=[1]
            for i in range(1,rowIndex):
                current=previous_row[i-1]+previous_row[i]
                curr.append(current)
            curr.append(1)

        return curr
        
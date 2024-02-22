class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        countOpen=0
        countClose=0

        for x in s:
            if x =="(":
                countOpen+=1
            elif x==")" and countOpen>0:
                countOpen-=1
            else:
                countClose+=1

        return (countOpen+countClose)
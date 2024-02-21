class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ySuffix=0
        nPrefix=0
        penalty=float("inf")
        ans=-1
        n=len(customers)
        for i in range(n):
            if customers[i]=="Y":
                ySuffix+=1

        for i in range(n + 1):
            prevInd = i - 1
            if prevInd >= 0:
                if customers[prevInd] == "Y":
                    ySuffix -= 1
                else:
                    nPrefix += 1
            
            if ySuffix + nPrefix < penalty:
                penalty = ySuffix + nPrefix
                ans = i
        
        return ans
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        checkString1={}
        checkString2={}
        minSum=float("inf")
        for indi,u in enumerate(list1):
            checkString1[u]=indi
        for index,y in enumerate(list2):
            checkString2[y]=index
        for key,value in checkString1.items():
            if key in checkString2:
                idxSum=(checkString1[key] + checkString2[key])
                minSum=min(minSum,idxSum)
        
        for key,value in checkString1.items():
            
            if key in checkString2:
                idxSum=(checkString1[key] + checkString2[key])
                if idxSum == minSum:
                    res.append(key)
        return res
                
        

                

        




        
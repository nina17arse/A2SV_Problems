class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic={}
        twentyFive=len(arr)//4
        res=0
        for x in arr:
            dic[x]=dic.get(x,0) + 1
        for key,value in dic.items():
            if value > twentyFive:
                res=key
        return res

        
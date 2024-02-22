class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        r=0
        dic={}
        partitionSizes=[]
        for i,v in enumerate(s):
            dic[v]=i
        #print(dic)
        for i, c in enumerate(s):
            r = max(r, dic[c])
            if i == r:
                partitionSizes.append(r - l + 1)
                l = r + 1

        return partitionSizes


                
        
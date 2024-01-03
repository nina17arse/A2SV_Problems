class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = {}
        for i in arr1:
            if i in x:
                x[i]+=1
            else:
                x[i]= 1
                
        out = []
        for i in arr2:
            for j in range(x[i]):
                out.append(i)
                x[i]-=1
        sorted_list = []
        for i in x:
            if x[i]>0:
                for j in range(x[i]):
                    sorted_list.append(i)
                    x[i]-=1
                    
        for i in range (1,len(sorted_list)):
            key = sorted_list[i]
            j = i-1
            while j>=0 and key <sorted_list[j]:
                sorted_list[j+1]=sorted_list[j]
                j-=1
            sorted_list[j+1]= key 
        return out + sorted_list
        
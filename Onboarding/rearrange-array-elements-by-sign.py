class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums=[]
        negativeNums=[]
        merged_list=[]
        for x in nums:
            if x >0:
                positiveNums.append(x)
            else:
                negativeNums.append(x)
        for i,j in zip(positiveNums,negativeNums):
            merged_list.append(i)
            merged_list.append(j)
        return merged_list
       
        
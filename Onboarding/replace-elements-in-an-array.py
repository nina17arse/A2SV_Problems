class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for i,val in enumerate(nums):
            dic[val] = i
        answer = nums
        for i,j in operations:
            index = dic[i]
            answer[index] = j
            dic.pop(i)
            dic[j] = index
        return answer 
        
        
                
                
        
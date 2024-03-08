class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        check=set()
        nums.sort()
        def sol_rec(nums, result, index, subArr): 
            if index == len(nums):
                check.add(tuple(subArr))
                result.append(subArr)
                return

            
            current_element = nums[index]

            sol_rec(nums, result, index + 1, subArr + [current_element])

            
            sol_rec(nums, result, index + 1, subArr)
        sol_rec(nums, result,0,[])
        

        
        return (list(c for c in check))
        
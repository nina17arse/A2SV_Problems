class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def sol_rec(nums, result, index, subArr): 
            if index == len(nums):
                result.append(subArr)
                return

            
            current_element = nums[index]

            sol_rec(nums, result, index + 1, subArr + [current_element])

            
            sol_rec(nums, result, index + 1, subArr)

        sol_rec(nums, result,0,[])

        return result


        



        

    


        
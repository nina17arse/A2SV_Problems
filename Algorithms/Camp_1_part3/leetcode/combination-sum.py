class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr=[]
        res=[]
        def sol_rec(i,s):
            if sum(curr)==target:
                res.append(curr.copy())
            else:
                if sum(curr)<target:
                    for y in range(i,len(candidates)):
                        curr.append(candidates[y])
                        sol_rec(y,sum(curr)+candidates[y])
                        curr.pop()

            return res

        return sol_rec(0,0)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def sol_rec(fn,sub):
            if len(sub) == k:
                ans.append(sub.copy())
                return
            for num in range(fn,n+1):
                sub.append(num)
                sol_rec(num+1,sub)
                sub.pop()

        ans=[]
        sol_rec(1,[])
        return ans
        
        
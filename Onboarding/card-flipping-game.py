class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalidNums=set()
        n=len(fronts)
        ans=[]
        for i in range(n):
            if fronts[i]==backs[i]:
                invalidNums.add(fronts[i])
        for k in range(n):
            if fronts[k] not in invalidNums:
                ans.append(fronts[k])
            if backs[k] not in invalidNums:
                ans.append(backs[k])
        if len(ans)==0:
            return 0
        else:
            return min(ans)
        # return 0 if ans == float("inf") else ans
        
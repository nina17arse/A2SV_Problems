class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        res=['']*n
        for idx in range(n):
            res[indices[idx]] = s[idx]
        return ''.join(res)
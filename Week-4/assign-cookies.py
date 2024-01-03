class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        count=0
        g.sort()
        s.sort()
        l=0
        r=0
        while l < n and r < len(s):
            if s[r]>=g[l]:
                l+=1
                r+=1
                count+=1
            else:
                r+=1
        return count
            



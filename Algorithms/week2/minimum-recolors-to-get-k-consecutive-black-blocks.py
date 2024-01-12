class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=-1
        ans=float("inf")
        countW=0
        for r, item in enumerate(blocks):
            if item=="W":
                countW+=1
            if r-l>=k:
                ans=min(ans,countW)
                l+=1
                countW-=blocks[l]=="W"
        return ans


            

        
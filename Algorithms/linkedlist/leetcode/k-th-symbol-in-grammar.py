class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current=0
        left,right = 0,2**(n-1)
        for _ in range(n-1):
            mid=(left+right)//2
            if k<=mid:
                right=mid
            else:
                left=mid + 1

                current=0 if current else 1

        return current
        
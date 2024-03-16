class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        "RECURSION"
        def sol_rec(s,start:int,end:int):
            if start>=end:
                return
            s[start],s[end]=s[end],s[start]

            sol_rec(s,start+1,end-1)

        sol_rec(s,0,len(s)-1)

        

        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        check=set()
        def sol_rec(r,c,i):
            if i == len(word):
                return True
            if (r <0 or c<0 or r >=row or c>=col or word[i]!=board[r][c]):
                return False
            if (r,c) in check:
                return False
            check.add((r,c))
            res=( sol_rec(r+1,c,i+1) or sol_rec(r,c+1,i+1) or sol_rec(r-1,c,i+1) or sol_rec(r,c-1,i+1))
            check.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if sol_rec(r,c,0):
                    return True
        return False
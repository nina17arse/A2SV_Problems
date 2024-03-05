class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        table={"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v",],
                "9":["w","x","y","z"]}
        
        def sol_rec(idx,path):
            if len(path) == len(digits):
                appended = ''
                for char in path:
                    appended += char
                answer.append(appended)
                return 
            if idx >= n:
                return
            
            for i in range(idx, n):
                for char in table[digits[i]]:
                    path.append(char)
                    sol_rec(i + 1, path)
                    path.pop()
        
        n = len(digits)
        answer = []
        if n == 0:
            return []
        sol_rec(0, [])

        return answer
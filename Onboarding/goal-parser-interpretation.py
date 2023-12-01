class Solution:
    def interpret(self, command: str) -> str:
        s= ""
        
        for index, letter in enumerate(command):
            if letter == "(" and command[index + 1] == ")":
                s += "o"
            elif letter == "(":
                s += "al"
            elif letter == "G":
                s += letter

        return s
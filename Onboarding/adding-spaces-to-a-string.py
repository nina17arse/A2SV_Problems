class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        str_length = len(s)
        num_spaces = len(spaces)
        start_index = 0
        ans = []

        for i in range(num_spaces):
            ans.append(s[start_index:spaces[i]])
            start_index = spaces[i]
        
        ans.append(s[spaces[num_spaces-1]:str_length])
        return ' '.join(ans)
        
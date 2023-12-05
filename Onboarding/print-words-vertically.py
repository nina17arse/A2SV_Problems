class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        
        result = []
        
        for i in range(max_len):
            column = ''
            for word in words:
                column += word[i] if i < len(word) else ' '
            result.append(column.rstrip())
        
        return result

        
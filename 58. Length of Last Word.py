class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed = s.rstrip()
        words = trimmed.split()

        if not words:
            return 0

        return len(words[-1])
            

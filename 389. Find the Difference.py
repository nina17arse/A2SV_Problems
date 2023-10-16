class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        frequency_s = {}
        frequency_t = {}

        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1

        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1

        for char in frequency_t:
            if frequency_t[char] > frequency_s.get(char, 0):
                return char

        return None

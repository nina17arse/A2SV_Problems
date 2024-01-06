class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        seen = set()
        max_length = 0

        while end < len(s):
            if s[end] in seen:
                seen.remove(s[start])
                start += 1
            else:
                seen.add(s[end])
                end += 1
                max_length = max(max_length, end - start)

        return max_length
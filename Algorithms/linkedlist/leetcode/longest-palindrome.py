class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(list(s))
        size = 0
        odd = 0
        for key in count:
            if count[key] % 2 == 0:
                size += count[key]
            else:
                size += (count[key] - 1)
                odd = 1
        if odd >0: 
            size += 1
        return size
        
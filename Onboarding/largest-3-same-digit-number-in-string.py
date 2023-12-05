class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_good_integer = ""

        for i in range(n - 2):
            substring = num[i:i+3]
            if len(set(substring)) == 1:
                max_good_integer = max(max_good_integer, substring)

        return max_good_integer
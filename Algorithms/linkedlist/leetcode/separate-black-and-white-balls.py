class Solution:
    def minimumSteps(self, s: str) -> int:
        NumOfOnes = 0
        ans = 0

        for balls in s:
            if balls == '1':
                NumOfOnes += 1
            else:
                ans += NumOfOnes

        return ans

        
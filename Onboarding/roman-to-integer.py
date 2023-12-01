class Solution:
    def romanToInt(self, s: str) -> int:
        key={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        values = list(map(lambda x: key[x], s))
        result = 0
        n = len(values)

        for i in range(n):
            if i < n - 1 and values[i] < values[i + 1]:
                result -= values[i]
            else:
                result += values[i]

        return result
                
        
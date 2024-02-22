class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        res = 0
        n = len(costs) // 2
        # print(costs)
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]
            #print(res)
        return res
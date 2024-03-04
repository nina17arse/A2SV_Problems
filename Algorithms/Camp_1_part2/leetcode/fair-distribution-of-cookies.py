class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        scores = [0]*k
        ans = [float("inf")]
        zero_counts = k
        print(scores)
        def backtrack(index, maxes, zero_counts):
            if zero_counts > n - index:
                return
            if index == n:
                ans[0] = min(ans[0], max(maxes))
                return
            for i in range(k):
                if not maxes[i]:
                    zero_counts -= 1
                maxes[i] += cookies[index]
                backtrack(index+1, maxes, zero_counts)
                maxes[i] -= cookies[index]
                if not maxes[i]:
                    zero_counts += 1
        backtrack(0, scores, zero_counts)
        return ans[0]
        
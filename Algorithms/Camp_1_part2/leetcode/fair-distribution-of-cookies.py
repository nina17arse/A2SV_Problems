class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0]*k
        n = len(cookies)        

        def sol_rec(i, zero_count):
            if n - i < zero_count:
                return float('inf')
            
            if n == i:
                return max(cur)
            
            answer = float('inf')
            for j in range(k): 
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]
                
                answer = min(answer, sol_rec(i+1, zero_count))

                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)

            return answer
        
        return sol_rec(0, k)
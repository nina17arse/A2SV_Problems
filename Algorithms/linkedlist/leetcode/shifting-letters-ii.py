class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # strOrd=[]
        # ans=""
        # timeline = [0] * (len(s) + 1)
        # curr=0

        # for start, end, direction in shifts:
        #     diff = 1 if direction else -1
        #     timeline[start] += diff
        #     timeline[end + 1] -= diff
        # for i in range(len(s)):
        #     strOrd.append(ord(s[i]))
        
        # for i in range(len(s)):
        #     curr+=timeline[i]
        #     strOrd[i]+=curr
            
        # for i in range(len(strOrd)):
        #     if strOrd[i]>=97 and strOrd[i] <=122:
        #         ans+=chr(strOrd[i])
        #     elif strOrd[i] <97:
        #         ans+=chr(strOrd[i]+26)
        #     elif strOrd[i]>122:
        #         ans+=chr(strOrd[i]-26)
            
        # return ans
        ans = []
        currShift = 0
        timeline = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            diff = 1 if direction else -1
            timeline[start] += diff
            timeline[end + 1] -= diff

        for i, c in enumerate(s):
            currShift = (currShift + timeline[i]) % 26
            num = (ord(s[i]) - ord('a') + currShift + 26) % 26
            ans.append(chr(ord('a') + num))

        return ''.join(ans)

            
            


        
        
        
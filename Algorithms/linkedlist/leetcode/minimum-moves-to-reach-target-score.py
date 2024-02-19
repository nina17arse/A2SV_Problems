class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        if maxDoubles==0:
            return target-1
        else:
            while target>1:
                if target%2!=0:
                    target-=1
                    count+=1
                elif target%2==0 and maxDoubles>0:
                    count+=1
                    maxDoubles-=1
                    target=target//2
                elif maxDoubles<=0:
                    break
            count+=target-1
        return count
        # if maxDoubles == 0: return target - 1
        # cnt = 0
        # while target != 1:
        #     if target % 2:
        #         target -= 1
        #         cnt += 1
        #     else:
        #         if maxDoubles == 0:
        #             break
        #         else:
        #             target = target // 2
        #             maxDoubles -= 1
        #             cnt += 1
        # cnt += target - 1
        # return cnt

        
        
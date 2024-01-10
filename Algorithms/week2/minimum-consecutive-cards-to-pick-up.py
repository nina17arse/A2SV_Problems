class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # size=float("inf")
        # for left in range(0,len(cards)-1):
        #     right=left+1
        #     if cards[left]!=cards[right]:
        #         right+=1
        #     elif cards[left]==cards[right]:
        #         size=min(size,right-left+1)
        #         r=l
        # return size if size < float("inf") else -1
        d={}
        min_value=len(cards)+1
        for i in range(len(cards)):
            if(cards[i] not in d):
                d[cards[i]]=i
            else:
                if(i - d[cards[i]] + 1 < min_value):
                    min_value = i - d[cards[i]] + 1
                d[cards[i]] = i
        if(min_value==len(cards)+1):
            return -1
        return min_value





        
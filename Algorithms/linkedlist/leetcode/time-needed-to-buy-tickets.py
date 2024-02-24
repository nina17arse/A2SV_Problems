class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        for i in range(len(tickets)):
            if tickets[i] - tickets[k] >=0 and k>=i:
                ans+=tickets[k]
            elif tickets[i] - tickets[k] >=0 and k<i:
                ans+=tickets[k]-1
            elif tickets[i]-tickets[k] <0:
                ans+=tickets[i]
        return ans

        
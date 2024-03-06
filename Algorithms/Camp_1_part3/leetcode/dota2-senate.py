class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        q1,q2=deque(),deque()
        for i,c in enumerate(senate):
            if c =="D":
                q1.append(i)
            else:
                q2.append(i)

        while q1 and q2:
            d1=q1.popleft()
            d2=q2.popleft()
            if d1 < d2:
                q1.append(d1+len(senate))
            else:
                q2.append(d2+len(senate))

        return "Radiant" if q2 else "Dire"
        
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
            r=0
            seen=[]
            count=0
            trainers.sort()
            players.sort()
            for i in range(len(players)):
                while r < len(trainers):
                    if trainers[r]<players[i]:
                        r+=1
                    else:
                        count+=1
                        r+=1
                        break
            return count if count>0 else 0

                        
        
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCount={}
        zeroLose=[]
        oneLose=[]
        for win,lose in matches:
              loseCount[win]=loseCount.get(win,0)
              loseCount[lose]=loseCount.get(lose,0) + 1
        for player,losses in loseCount.items():
          if losses==0:
            zeroLose.append(player)
          elif losses==1:
            oneLose.append(player)
        return [sorted(zeroLose),sorted(oneLose),]   
        
    
                

            
        
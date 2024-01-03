class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team1=[]
        l=0
        r=len(skill)-1
        prefixSum=0
        while l < r:
            if skill[r]+skill[l]==skill[r-1]+skill[l+1]:
                team1.append((skill[l],skill[r]))
            l+=1
            r-=1
            
            
        if len(team1) != len(skill)/2:
            return -1
        else:
            products = [1] * len(team1) 
            for i, t in enumerate(team1):
                for num in t:
                    products[i] *= num

                prefixSum+=products[i]
            return prefixSum
                    
                    
                        
        
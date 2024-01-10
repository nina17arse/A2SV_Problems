class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size=len(p)
        target=Counter(p)
        wind=Counter(s)
        count=[]
        for i in range(len(s)):
            window=Counter(s[i:i+size])
            if window==target:
                count.append(i)
        return count

        
               
        


        
            
        
        
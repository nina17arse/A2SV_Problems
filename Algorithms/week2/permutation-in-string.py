class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ordmap = [0]*26
        for i in s1:
            ordmap[ord(i) - ord('a')] += 1
        for i in range(len(s2)-len(s1)+1):
            ordmap1 = [0]*26
            for char in s2[i:i+len(s1)]:
                ordmap1[ord(char)-ord('a')] += 1
            if ordmap1 == ordmap: return True
        return False


        
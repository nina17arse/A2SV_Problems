class Solution:
    def freqAlphabets(self, s: str) -> str:
        dictionary={}
        outString=""
        i=0
        
        for p, letter in enumerate(range(ord('a'), ord('i') + 1), start=1):
            dictionary[(str(p))] = chr(letter)
        for k, letter in enumerate(range(ord('j'), ord('z') + 1), start=10):
            dictionary[(str(k)+"#")] = chr(letter)
        
        while i<len(s):
            if (i+2)<len(s) and s[i+2]=="#":
                if s[i:i+3] in dictionary:
                    outString+=(dictionary[s[i:i+3]])
                    i+=3
            else:
                outString+=(dictionary[s[i]])
                i+=1

        return outString
        
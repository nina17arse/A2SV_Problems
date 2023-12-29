class Solution:
    def sortSentence(self, s: str) -> str:
        string_list=s[::-1].split()
        string_list.sort()
        res=[]
        for i in string_list:
            res.append(i[1:][::-1])
        return " ".join(res)
        
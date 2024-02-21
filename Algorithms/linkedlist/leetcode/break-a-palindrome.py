class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        list_letters=list(palindrome)
        for i in range(int(len(list_letters)/2)):
            if list_letters[i]!="a":
                list_letters[i]='a'
                return "".join(list_letters)
        list_letters[len(list_letters)-1] = 'b'
        if len(list_letters)>1:
            return "".join(list_letters)
        else:
            return ""
    #A EXPERIMENTAL SOLUTION USING DICTIONARY AND ORD,CHR FUNCTIONS 
      #FAILS AT PALINDROME="aa"
        # dic_ords={}
        # dic_str={}
        # min_ord=float("inf")
        # res=[]
        # ans=""
        # for i in range(97,123):
        #     dic_ords[chr(i)]=i
        # for i in range(len(palindrome)):
        #     dic_str[palindrome[i]]=ord(palindrome[i])
        # for i in range(1,len(palindrome)):
        #     if palindrome[i]=="a" and i==0:
        #         pass
        #     else:
        #         min_ord=min(min_ord,ord(palindrome[i]))
        # for i in range(len(palindrome)):
        #     if ord(palindrome[i])!=min_ord:
        #         res.append(palindrome[i])

        #     elif ord(palindrome[i])==min_ord and min_ord>97:
        #         res.append(chr(dic_ords[chr(min_ord-1)]))
        #         res.append(palindrome[i+1: ])
        #         ans="".join(res)
        #         break

        # return ans

        

        
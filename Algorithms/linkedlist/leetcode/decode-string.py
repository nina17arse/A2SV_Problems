class Solution:
    def decodeString(self, s: str) -> str:
        def helper(idx:int):
            result = ""
            count = 0

            while idx < len(s):
                if s[idx].isdigit():
                    count = count * 10 + int(s[idx])
                    idx += 1
                elif s[idx] == '[':
                    decoded, idx = helper(idx + 1)
                    result += count * decoded
                    count = 0
                elif s[idx] == ']':
                    return result, idx + 1
                else:
                    result += s[idx]
                    idx += 1

            return result, idx

        return helper(0)[0]















# :
#         num = 0
#         res = []
#         def helper(s,start):
#             temp = ''
#             while start < len(s):
#                 if s[start] == ']' or start == len(s) -1:
#                     start += 1
#                     return temp
#                 elif s[start].isdigit():
#                     num = int(s[start])
#                 elif s[start] == '[':
#                     resFunc = helper(s,start+1)
#                     for i in range(num):
#                         res.append( resFunc )
#                     return ''.join(res)
#                 else:
#                     temp += s[start]
#                 start += 1
#         return helper(s,0)


        
            

            

        


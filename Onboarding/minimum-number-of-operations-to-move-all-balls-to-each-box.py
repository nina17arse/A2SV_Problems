class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for x in range(len(boxes)):
            count=0
            for y in range(len(boxes)):
                if boxes[y]=='1':
                    count+=abs(y-x)
            ans.append(count)
        return ans
        
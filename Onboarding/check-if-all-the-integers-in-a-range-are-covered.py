class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        setRanges=set()
        for start,end in ranges:
          for p in range(start,end+1):
            setRanges.add(p)

        for i in range(left,right+1):
          if i not in setRanges:
            return False
          
        return True
            

        
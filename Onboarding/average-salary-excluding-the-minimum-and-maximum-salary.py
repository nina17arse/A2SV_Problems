class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avgSum=[]
        last=len(salary)-1
        for x in range(0,len(salary)):
            if x==0:
                continue
            elif x==last:
                continue
            else:
                avgSum.append(salary[x])
            avg=sum(avgSum)/(len(salary)-2)
        return avg
        
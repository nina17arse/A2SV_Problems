class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    countOf5 = 0
    countOf10 = 0
    # countOf20
    if bills[0]!=5:
        return False
    for bill in bills:
      if bill == 5:
        countOf5 += 1
      elif bill == 10:
        countOf5 -= 1
        countOf10 += 1
      else:  # bill == 20
        if countOf10 > 0:
          countOf10 -= 1
          countOf5 -= 1
        else:
          countOf5 -= 3
      if countOf5 < 0:
        return False

    return True
    # n=len(bills)
    #     if bills[0]!=5:
    #         return False
    #     count=0
    #     for i in range(n):
    #         bills[i]=bills[i]//5
    #         if bills[i]==1:
    #             count+=1
    #         else:


    #     print(bills)
        
        
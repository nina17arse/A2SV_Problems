class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        m=num%3
        n=int(num/3)
        if m !=0:
            return []
        elif m==0:
            return[(n-1),(n),(n+1)]
            
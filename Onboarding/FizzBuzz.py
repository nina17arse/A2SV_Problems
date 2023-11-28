class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result =[]
        for x in range(1, n+1):
            temperory = ''
            if x % 3 == 0:
                temperory += 'Fizz'
            if x % 5 == 0:
                temperory += 'Buzz'
            
            if x % 3 != 0 and x % 5 != 0:
                temperory += f'{x}'
            result.append(temperory)
        return result        

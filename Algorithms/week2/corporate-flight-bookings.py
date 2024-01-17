class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        numSeats=[0] * (n+1)
        for start,last,seats in bookings:
            numSeats[start-1]+=seats
            numSeats[last] -=seats
            # right+=seats
        # print(numSeats)
        ans=[]
        res=0
        for i in range(0,len(numSeats)-1):
            res+=numSeats[i]
            ans.append(res)
        return ans
            
            

        
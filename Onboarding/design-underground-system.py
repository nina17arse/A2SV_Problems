class UndergroundSystem:

    def __init__(self):
        self.checkin={}
        self.total_times={}
        self.countCust={}
        self.res=0
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName,t)
        
        

        
        


        
        
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,timeStart = self.checkin[id]
        
        travel_time=t-timeStart
        
        
        if (start, stationName) in self.total_times:
            self.total_times[(start, stationName)] += travel_time
            # print(self.total_times)
            self.countCust[(start, stationName)] += 1
        else:
            self.total_times[(start, stationName)] = travel_time
            self.countCust[(start, stationName)] = 1

        
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalDuration= self.total_times[(startStation, endStation)]
        maxCount=self.countCust[(startStation, endStation)]
        self.res=totalDuration/maxCount
        return self.res
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
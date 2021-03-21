#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3678/
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkins={}
        self.avgTime=defaultdict(lambda:(0,0)) #tuple of 0,0

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id]=(stationName,t)

    def checkOut(self, id: int, currentStationName: str, t: int) -> None:
        startStationName,t0=self.checkins[id]
        duration=t-t0
        key=(startStationName,currentStationName)
        self.avgTime[key]=(self.avgTime[key][0]+duration,self.avgTime[key][1]+1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key=(startStation,endStation)
        total,n=self.avgTime[key]
        return total/n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
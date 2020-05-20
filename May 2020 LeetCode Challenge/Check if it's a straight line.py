#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1=coordinates[0][0],coordinates[0][1]
        x2,y2=coordinates[1][0],coordinates[1][1]
        #same slope or x=k or y=k
        if(x1==x2):
            #since slope will be infinity!
            #x=k
            for i in range(2,len(coordinates)):
                x=coordinates[i][0]
                if(x!=x1):
                    return False
        else:
            #slope can be found
            #note y=k will have slope 0
            m=(y2-y1)/(x2-x1)
            for i in range(2,len(coordinates)):
                x2,y2=coordinates[i][0],coordinates[i][1]
                current_m=(y2-y1)/(x2-x1)
                if(current_m!=m):
                    return False
                
        return True
        
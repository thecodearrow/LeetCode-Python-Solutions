#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3778/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #knapsack greedy like
        #sort by units (second idx)
        boxTypes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        ans=0
        #from each box type, take as much as possible!
        for w,val in boxTypes:
            if(truckSize==0):
                break
            taken_wt=min(truckSize,w)
            ans+=(taken_wt)*val
            truckSize-=taken_wt
        
            
        
        return ans
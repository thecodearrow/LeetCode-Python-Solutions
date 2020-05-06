#https://leetcode.com/contest/weekly-contest-185/problems/display-table-of-food-orders-in-a-restaurant/a

from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        row1=["Table"]
        count={}
        foods=set()
        table=set()
        for cName,tNum,foodName in orders:
            foods.add(foodName)
            if(tNum not in count):
                count[tNum]=defaultdict(lambda:0)
            count[tNum][foodName]+=1
            table.add(int(tNum))
        foods=sorted(list(foods))
        table=sorted(list(table))
        table=[str(t) for t in table]
        for f in foods:
            row1.append(f)
        
        ans=[row1]
        for t in table:
            
            row=[t]
            for f in foods:
                row.append(str(count[t][f]))
            ans.append(row)
        return ans
                
            
            
            
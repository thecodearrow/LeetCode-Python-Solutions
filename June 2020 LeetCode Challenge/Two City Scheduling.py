"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.



Approach--
 Think of this way...
 You're thinking of flying every person to city B but suddenly you're offerred a bonus/refund of (a-b) if you fly this person to city A
 
 You would want to keep this value negative and large since if it's positive you'll have to pay for it. 

Hence sorting based on (a-b) works! 

"""


        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        min_cost=0
        new_costs=[(a,b,a-b) for a,b in costs]
        new_costs=sorted(new_costs,key=lambda x:x[2])
        idx=1
        for cost_a,cost_b,_ in new_costs:
            if(idx<=n//2):
                #first n//2 would be flown to city A
                #since i'll get the maximum possible refund
                min_cost+=cost_a
            else:
                #next n//2 would be flown to city B
                 min_cost+=cost_b
            idx+=1
            
        
        return min_cost
        
            
        
        
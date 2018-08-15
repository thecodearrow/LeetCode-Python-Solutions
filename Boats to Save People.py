#Two pointer Greedy solution

class Solution:

	#Sort the people's weights 

	#Try pairing greedily a lighter one and a heavier one 

	#If that doesn't work, let the heavier one have the boat 

	#DONE :)
	
    def numRescueBoats(self, people, limit):
        people=sorted(people)
        start=0
        end=len(people)-1
        boats=0
        while(start<=end):
            boats+=1
            one=people[start]
            two=people[end]
            if(one+two<=limit):
                start+=1
                end-=1
            else:
                end-=1
                
            
                    
        
        return boats
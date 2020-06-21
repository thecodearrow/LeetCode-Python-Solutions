"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/discuss/673519/Python-O(N2)-6-lines-of-code

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people=sorted(people,key=lambda x:(-x[0],x[1]))
        for h,i in people:
            current_person=[h,i]
            people.remove(current_person)
            people.insert(i,current_person)  
        return people
            
        
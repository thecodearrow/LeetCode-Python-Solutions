#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count=Counter(s)
        char_count_array=[[c,char_count[c]] for c in char_count] #(c,count)
        res_string=[]
        char_count_array=sorted(char_count_array,key=lambda x: x[1], reverse=True)
        for c,count in char_count_array:
            for i in range(count):
                res_string.append(c)
                
        return "".join(res_string)
            
        
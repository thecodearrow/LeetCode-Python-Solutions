#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/
class Solution(object):
    def groupAnagrams(self, strs):
        ans=[]
        seen_strings={}
        index=0
        for s in strs:
            sorted_string="".join(sorted(s))
            if(sorted_string in seen_strings):
                string_index=seen_strings[sorted_string]
                ans[string_index].append(s)
            else:
                seen_strings[sorted_string]=index
                ans.append([s])
                index+=1
                
        return ans
            
            
            
        
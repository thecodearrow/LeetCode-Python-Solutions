#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#Implemented using the sliding window technique 

class Solution:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        slider1=0
        slider2=0
        seen_at={}
        current_L=0
        maxL=0
        
        while(slider1<n and slider2<n):
            ele=s[slider2]
            if(ele not in seen_at or seen_at[ele]<slider1):
                current_L+=1
            else:
                prev_slider1=slider1
                slider1=seen_at[ele]+1
                moved=slider1-prev_slider1
                current_L=current_L-moved+1
            
            seen_at[ele]=slider2
            if(maxL<current_L):
                maxL=current_L
            slider2+=1

        return maxL
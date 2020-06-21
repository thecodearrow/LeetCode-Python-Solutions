#https://leetcode.com/problems/next-greater-element-i/submissions/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        stack=[]
        next_great={}
        for ele in nums2[::-1]:
            while stack and stack[-1]<ele:
                stack.pop()
            if(stack):
                next_great[ele]=stack[-1]
            else:
                next_great[ele]=-1
            
            stack.append(ele)
        for ele in nums1:
            ans.append(next_great[ele])
        return ans
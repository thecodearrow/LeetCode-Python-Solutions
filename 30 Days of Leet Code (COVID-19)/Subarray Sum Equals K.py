#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        sum_seen={0:1}
        current_sum=0
        for i in range(n):
            current_sum+=nums[i]
            needed_sum=current_sum-k
            if(needed_sum in sum_seen):
                count+=sum_seen[needed_sum]
            if(current_sum not in sum_seen):
                sum_seen[current_sum]=1
            else:
                sum_seen[current_sum]+=1
        return count
        
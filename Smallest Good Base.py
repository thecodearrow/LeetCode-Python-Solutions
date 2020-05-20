#https://leetcode.com/problems/smallest-good-base/submissions/

"""

Credits to Kshitij Mishra from Scaler Academy

/*
 * Smallest Good Base
 * For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.
 * Now given a string representing n, you should return the smallest good base of n in string format.
 *
 *
 * Basic Observations:
 * Any number N when represented in base the (N-1), will always be 11.
 *
 * 3 in base 2 -> 11
 * 4 in base 3 -> 11
 * 5 in base 4 -> 11
 * .
 * .
 * .
 * and so on
 *
 * Why? 
 * 11 => 1*base^0 + 1*base^1
 * this should be equal to N
 * => N = 1*base^0 + 1*base^1
 * => base = N-1
 *
 * So, the maximum value of the Good Base will be N-1.
 * What could be the minimum value? 
 * min val = 2 (We have to find the actual minimum value but the lowest possible value that the ans can take is 2)
 *
 * So we have the ans space ranging from [2, N-1]
 *
 * How to find the smallest good base now?
 *
 * Brute force:
 *
 * Iterate over the ans space and check if the ith element is a good base or not.
 * TC: 
 * O(N) -> Iterating over the array
 * O(Log N) -> Checking if the ith no is a good base.
 * Total TC O(NlogN)
 *
 * How to optimize?
 *
 * Let us analyse how the brute force is working:
 * For any number N  we are iterating from 2 to N-1 till we find the good base.
 * check if 2 is a good base 
 * check if 3 is a good base
 * .
 * .
 * .
 * check if N-1 is a good base
 *
 * If you observe,we are doing a linear search over the answer.
 * We also have the ans space with us. Let us see if we can discard a part of the ans space.
 *
 * For a number N, 
 * if m is a good base,
 *     Do we need to check for any value greater than m?
 *     No! We have to find the smallest good base.
 *     We can discard the right half of the ans space in this case.
 *
 * else if m is NOT a good base
 *     Can we discard a part of the ans space in this case?
 *     Can we say that if m is not a good base then any number greater than m will also not be good base?
 *     Or Can we say that if m is not a good base then any number less than m will also not be a good base?
 *
 *     NO!
 *     See an exmaple:
 *     For N=13,
 *     m=6 is NOT a good base,
 *     but 12 and 3 are good base.
 *     So the ans can be found on any side of m.
 *     We can not make the decision to discard a part of the search space in this case!
 * 
 * Why?  What is it that is not allowing us to make any desicion here?
 * It is "the number of digits"
 * Yes. Different bases can be good bases for a number for different number of digits.
 *
 * for 13
 * 3 is a good base, 13 in base 3 is "1 1 1"
 * 12 is also a good base, 13 in base 12 is "1 1"
 * a larger number can be a good base with lesser number of digits
 * and a smaller can be a good base with more number of digits
 *
 * What if we fix the number of digits!
 * will that help us in making a decision to discard a part of the search space?
 *
 * Lets say that we are only finding a good base for d digits (i.e. the number when represented in the good base should have exactly d digits)
 * Which means ther that the number N when represented in the good base will be, 1 1 1 1 1 .....d times
 *
 * Can we now make a decision for d digits?
 *
 * if m is a base, and number of digits fixed to d
 * then the number would be
 *
 * num = 1*m^0 + 1*m^1 + 1*m^2 + ... + 1*m^(d-1)
 * 
 * if num == n
 *    m is a good base
 *    we don't need to check for any value >m
 *    right half of the ans space can be discarded
 *
 * if num < n
 *    we need to increase the value of m
 *    discard the left part of the ans space
 *
 * if num > n
 *    we need to reduce the value of m
 *    discard the right part of the ans space
 *    
 * So now, we have a monotous function
 *
 * isPossible(base B, digits d, number N) -> Returns true if the number N in base B can be represented as 11111...d times
 *
 * Can we apply binary search to find the ans for a given number of digits now?
 *
 * Yes :)
 *
 * If we do it for all possible number of digits, the min goodbase becomes the ans.
 * What would be the maximum number of digits??
 * Will that be same as the number of digits in the smallest possible base?
 * What is the smallest possible base?
 * Think ;)
 *
 * Time Complexity: 
 * O(log N) -> finding a good base for a fixed number of digits
 * O(Number of digits) -> for doing the above for all possible digit sizes.
 * 
 * Total TC: O(D*D*log N) (Where D is the maximum number of digits you can have)
 *
 */
"""

import math
class Solution:
    # @param A : string
    # @return a strings
    
    def allOnes(self,l,b):
        #returns the value of (1111...l times) base b
        power_b=1
        number=0
        for i in range(l):
            number+=power_b
            power_b*=b
            
        return number
            
    def findGoodBase(self,A,l):
        start=2
        end=A-1 #max possible base is A-1 and it is always a good base!
        status=False
        base=None
        while start<=end:
            mid=start+(end-start)//2
            value=self.allOnes(l,mid)
            if(value==A):
                return mid,True #base found
            if(value<A):
                #increase base!
                start=mid+1
            else:
                end=mid-1
            
        return base,status
            
    def smallestGoodBase(self, A: str) -> str:
        A=int(A)
        min_base=A-1
        digits=math.ceil(math.log2(A))
        for l in range(1,digits+1):
            #We're going in reverse because larger the l, smallest is the value of goood base! (and we have to return min good base)
            #for every l try to find a good base if it exists! 
            gb,status=self.findGoodBase(A,l)
            if(status):
                min_base=min(min_base,gb)
             
            
        
        return str(min_base)
                
        



    
        
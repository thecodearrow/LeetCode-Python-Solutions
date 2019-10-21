#https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0/

t=int(input())
while t!=0:
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    seen_sum={0:-1} #where was it seen
    cum_sum=0
    zero_sum=False
    for i in range(len(a)):
        cum_sum+=a[i]
        if(cum_sum in seen_sum):
            zero_sum=True
            break
        else:
            seen_sum[cum_sum]=i
            
    if(zero_sum):
        print("Yes")
    else:
        print("No")

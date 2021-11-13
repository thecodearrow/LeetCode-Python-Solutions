class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        global ans
        ans=[]
        def generate(current,i,o,e):
            if(i==2*n):
                global ans
                ans.append("".join(current))
                return 
            if(o<n):
                generate(current+['('],i+1,o+1,e)
            if(o>e):
                generate(current+[')'],i+1,o,e+1)
        generate([],0,0,0)
        return ans

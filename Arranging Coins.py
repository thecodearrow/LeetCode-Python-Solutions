class Solution:
    def arrangeCoins(self, n: int) -> int:
        r=(math.sqrt(1+8*n)-1)/2
        return int(r)
    

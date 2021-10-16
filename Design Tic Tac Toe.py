class TicTacToe:

    def __init__(self, n: int):
        self.n=n
        self.row=defaultdict(lambda:0) 
        self.col=defaultdict(lambda:0) 
        self.primary=defaultdict(lambda:0)  #primary diagonal
        self.secondary=defaultdict(lambda:0)  #secondary diagonal
        

    def move(self, r: int, c: int, player: int) -> int:
        n=self.n
        row=self.row
        col=self.col
        primary=self.primary
        secondary=self.secondary
        if(player==1):
            #move = +1 for player 1
            row[r]+=1
            col[c]+=1
            d=r-c
            s=r+c
            primary[d]+=1 #primary diagonal
            secondary[s]+=1 #secondarys diagonal
            if(row[r]==n or col[c]==n or primary[d]==n or secondary[s]==n):
                return 1
        else:
            #move = -1 for player 2
            row[r]-=1
            col[c]-=1
            d=r-c
            s=r+c
            primary[d]-=1 #primary diagonal
            secondary[s]-=1 #secondarys diagonal
            if(row[r]==-n or col[c]==-n or primary[d]==-n or secondary[s]==-n):
                return 2
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

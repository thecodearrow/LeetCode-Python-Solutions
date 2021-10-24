class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        #a snake is just an ordered collection of cells.
        
        self.width=width
        self.height=height
        self.food=food 
        self.food_index=0
        self.score=0
        self.snake=deque([(0,0)]) #dequeue would be ideal to store all the snake cells! 
        self.snake_set=set() #set to store snake cells! 
        self.snake_set.add((0,0))
    def outOfBounds(self,i,j):
        if(i<0 or j<0 or i==self.height or j==self.width):
            return True
        return False
        
    def getNewHeadPos(self,direction,i,j):
        if(direction=="D"):
            return i+1,j
        elif(direction=="U"):
            return i-1,j
        elif(direction=="L"):
            return i,j-1
        elif(direction=="R"):
            return i,j+1
    def snakeBitesItself(self,head_i,head_j):
        #we can do this in O(1) with the help of a set!
        return (head_i,head_j) in self.snake_set
        # snake_cells=list(self.snake)
        # snake_cells.pop() #except head
        # for i,j in snake_cells:
        #     if(i==head_i and j==head_j):
        #         return True
        #return False
            
        
        
    def move(self, direction: str) -> int:
        head_i,head_j=self.snake[-1]
        head_i,head_j=self.getNewHeadPos(direction,head_i,head_j) #update snake head pos
        if(self.outOfBounds(head_i,head_j)):
            return -1
        tail_i,tail_j=self.snake.popleft()
        self.snake_set.remove((tail_i,tail_j)) #if snake isn't growing, we remove the tail cell! 
        if(self.food_index<len(self.food)):
            #check for food cell and grow snake when possible! 
            food_i,food_j=self.food[self.food_index]
            if((head_i,head_j)==(food_i,food_j)):
                #contains food! 
                self.snake.appendleft((tail_i,tail_j)) #add the tail back since size+=1
                self.snake_set.add((tail_i,tail_j))
                self.food_index+=1
                self.score+=1
        
        if(self.snakeBitesItself(head_i,head_j)):
            return -1
        self.snake.append((head_i,head_j)) #add updated head to snake cell list!
        self.snake_set.add((head_i,head_j)) #add the new updated head to snake cell set! 

        return self.score
        
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

class Twitter:
    def __init__(self):
        self.tweets=[] #most recent tweets by {user_id, tweetId}
        self.user_info=defaultdict(set) #has info by user_id on users he follows
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet={"userId":userId,"tweetId":tweetId}
        self.tweets.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        required_count=10
        n=len(self.tweets)
        last_10=[]
        count=0 #get 
        for i in range(n-1,-1,-1):
            user_id=self.tweets[i]["userId"]
            tweet_id=self.tweets[i]["tweetId"]
            if(user_id==userId or user_id in self.user_info[userId]):
                #posted by users who the user followed or by the user themself.
                last_10.append(tweet_id)
                count+=1
                if(count==required_count):
                    return last_10
        return last_10

    def follow(self, followerId: int, followeeId: int) -> None:
        if(followeeId not in self.user_info[followerId]):
            self.user_info[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.user_info[followerId]):
            self.user_info[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

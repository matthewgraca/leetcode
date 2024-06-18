from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.posts = {}     # {userId: set((time, tweetId))}
        self.follows = {}   # {followerId: set(followees)} 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = set()
        self.posts[userId].add((self.time, tweetId))
        self.time -= 1  # reversing time so min heap has most recent tweet on top
        
    '''
        Retrieves 10 most recent tweet IDs in userId's feed.
        Can only pull from userId's follows or userId themself.
        Ordered from most recent to least recent
    '''
    def getNewsFeed(self, userId: int) -> List[int]:
        # get user's list of follows
        followedIdList = []
        if userId in self.follows:
            followedIdList = self.follows[userId]

        # get a list of followeds' tweets
        # for each follower, get their posts. for each post, add to feed 
        totalFeed = []
        for followedId in followedIdList:
            if followedId in self.posts:
                followedPosts = self.posts[followedId] # (time, tweetId)
                for timeAndTweetId in followedPosts:
                    totalFeed.append(timeAndTweetId)

        # get user's list of tweets
        if userId in self.posts:
            userPosts = self.posts[userId]
            for timeAndTweetId in userPosts:
                totalFeed.append(timeAndTweetId)

        # combine follower tweets with user tweets in a time min heap 
        heapq.heapify(totalFeed)
        topTen = []
        while totalFeed and len(topTen) < 10:
            time, tweetId = heapq.heappop(totalFeed)
            topTen.append(tweetId)

        return topTen 
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)

    '''
        Helper functions for testing
    '''

    def getFollowList(self) -> dict:
        return self.follows

    def getPostList(self) -> dict:
        return self.posts

'''
need to make the tweets of a user sortable (by some time variable)

want to update the users's total feed as they add follows and unfollow

'''

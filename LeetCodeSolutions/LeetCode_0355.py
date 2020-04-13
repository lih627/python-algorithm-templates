from collections import defaultdict, deque
from heapq import heappop, heappush, nlargest


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = defaultdict(set)
        self.users_tweet = {}
        self.uid = 0

    def _create_user(self, userId):
        self.users[userId].add(userId)
        self.users_tweet[userId] = deque(maxlen=10)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self._create_user(userId)
        self.users_tweet[userId].appendleft((self.uid, tweetId))
        self.uid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users:
            self._create_user(userId)
        all_users = list(self.users[userId])
        # num_each_posted = [len(self.users_tweet[user_id]) for user_id in all_users]
        heap = []
        for user_id in all_users:
            for item in self.users_tweet[user_id]:
                heappush(heap, item)
        ret = [x[1] for x in nlargest(10, heap)]
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.users:
            self._create_user(followeeId)
        if followerId not in self.users:
            self._create_user(followerId)
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.users:
            self._create_user(followeeId)
        if followerId not in self.users:
            self._create_user(followerId)
        if followerId != followeeId and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

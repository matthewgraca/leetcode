import unittest
from src.heap.design_twitter import Twitter

class DesignTwitterTest(unittest.TestCase):
    def test_init(self):
        twt = Twitter()
        self.assertTrue(True)

    def test_successfully_added_follower(self):
        twt = Twitter()
        twt.follow(0, 100)
        actual = twt.getFollowList()
        expected = {0: set([100])}
        self.assertEqual(actual, expected)

    def test_successfully_remove_follower(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.unfollow(0, 100)
        actual = twt.getFollowList()
        expected = {0: set()}
        self.assertEqual(actual, expected)

    def test_if_follower_already_added_another_is_not_added(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.follow(0, 100)
        actual = twt.getFollowList()
        expected = {0: set([100])}
        self.assertEqual(actual, expected)

    def test_no_follower_removed_if_not_in_list(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.unfollow(1, 100)
        actual = twt.getFollowList()
        expected = {0: set([100])}
        self.assertEqual(actual, expected)

    def test_multiple_followers_with_same_followee(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.follow(1, 100)
        actual = twt.getFollowList()
        expected = {0: set([100]), 1: set([100])}
        self.assertEqual(actual, expected)

    def test_one_id_many_followers(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.follow(0, 200)
        actual = twt.getFollowList()
        expected = {0: set([100,200])}
        self.assertEqual(actual, expected)

    def test_one_id_many_followers_one_remove(self):
        twt = Twitter()
        twt.follow(0, 100)
        twt.follow(0, 200)
        twt.unfollow(0, 100)
        actual = twt.getFollowList()
        expected = {0: set([200])}
        self.assertEqual(actual, expected)

    def test_posts_successfully_added(self):
        twt = Twitter()
        twt.postTweet(0, 1001)
        actual = twt.getPostList()
        expected = {0: set([(0,1001)])}
        self.assertEqual(actual, expected)

    def test_multiple_posts_successfully_count_time(self):
        twt = Twitter()
        twt.postTweet(0, 1001)
        twt.postTweet(0, 1002)
        twt.postTweet(0, 1003)
        twt.postTweet(11, 123)
        actual = twt.getPostList()
        expected = {0: set([(0,1001),(-1,1002),(-2,1003)]), 11: set([(-3,123)])}
        self.assertEqual(actual, expected)

    def test_example1(self):
        twitter = Twitter()
        twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
        test1 = twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        self.assertEqual(test1, [5])

        twitter.follow(1, 2)    # User 1 follows user 2.
        twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
        test2 = twitter.getNewsFeed(1)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        self.assertEqual(test2, [6,5])

        twitter.unfollow(1, 2)  # User 1 unfollows user 2.
        test3 = twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
        self.assertEqual(test3, [5])

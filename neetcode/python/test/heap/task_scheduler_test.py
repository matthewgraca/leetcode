import unittest
from src.heap.task_scheduler import Solution

class TaskSchedulerTest(unittest.TestCase):
    def test_example1(self):
        tasks, n = ["A","A","A","B","B","B"], 2
        actual = Solution().leastInterval(tasks, n)
        expected = 8
        self.assertEqual(actual, expected)

    def test_example2(self):
        tasks, n = ["A","C","A","B","D","B"], 1
        actual = Solution().leastInterval(tasks, n)
        expected = 6 
        self.assertEqual(actual, expected)

    def test_example3(self):
        tasks, n = ["A","A","A", "B","B","B"], 3
        actual = Solution().leastInterval(tasks, n)
        expected = 10 
        self.assertEqual(actual, expected)

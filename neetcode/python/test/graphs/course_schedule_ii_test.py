import unittest
from src.graphs.course_schedule_ii import Solution

class CourseScheduleIITest(unittest.TestCase):
    def test_example1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        actual = Solution().findOrder(numCourses, prerequisites)
        expected = [0,1]
        self.assertEqual(actual, expected)

    def test_example2(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        actual = Solution().findOrder(numCourses, prerequisites)
        expectedA = [0,2,1,3]
        expectedB = [0,1,2,3]
        expected1, expected2 = True, True
        for i in range(len(expectedA)):
            if actual[i] != expectedA[i]:
                expected1 = False
        for i in range(len(expectedB)):
            if actual[i] != expectedB[i]:
                expected2 = False
        expected = expected1 or expected2
        self.assertTrue(expected)

    def test_example3(self):
        numCourses = 1 
        prerequisites = []
        actual = Solution().findOrder(numCourses, prerequisites)
        expected = [0]
        self.assertEqual(actual, expected)

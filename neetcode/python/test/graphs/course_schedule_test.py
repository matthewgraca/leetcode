import unittest
from src.graphs.course_schedule import Solution

class CourseScheduleTest(unittest.TestCase):
    def test_example1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        actual = Solution().canFinish(numCourses, prerequisites)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        actual = Solution().canFinish(numCourses, prerequisites)
        expected = False 
        self.assertEqual(actual, expected)


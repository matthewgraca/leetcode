import unittest
from src.stack.car_fleet import Solution

class CarFleetTest(unittest.TestCase):
    def test_example1(self):
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]
        actual = Solution.carFleet(target, position, speed)
        expected = 3
        self.assertEqual(actual, expected)

    def test_example2(self):
        target = 10
        position = [3]
        speed = [3]
        actual = Solution.carFleet(target, position, speed)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example3(self):
        target = 100
        position = [0,2,4]
        speed = [4,2,1]
        actual = Solution.carFleet(target, position, speed)
        expected = 1
        self.assertEqual(actual, expected)

    def test_example4(self):
        target = 10
        position = [8,3,7,4,6,5]
        speed = [4,4,4,4,4,4]
        actual = Solution.carFleet(target, position, speed)
        expected = 6
        self.assertEqual(actual, expected)

    def test_example5(self):
        target = 31
        position = [5,26,18,25,29,21,22,12,19,6]
        speed = [7,6,6,4,3,4,9,7,6,4]
        actual = Solution.carFleet(target, position, speed)
        expected = 6
        self.assertEqual(actual, expected)

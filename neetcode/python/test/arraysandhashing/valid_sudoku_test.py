import unittest
from typing import List
from src.arraysandhashing.valid_sudoku import Solution

class ValidSudokuTest(unittest.TestCase):
    def test_example1(self):
        board = ( 
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        )
        actual = Solution.isValidSudoku(board)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        board = ( 
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        )
        actual = Solution.isValidSudoku(board)
        expected = False 
        msg = "Fails: more than one '8' in the first column" 
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        board = ( 
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","5",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        )
        actual = Solution.isValidSudoku(board)
        expected = False 
        msg = "Fails: more than one '5' in the first block"
        self.assertEqual(actual, expected, msg)

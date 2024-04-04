from typing import List

class Solution:
    def isValidSudoku(board: List[List[str]]) -> bool:
        rows = 9
        cols = 9
        block1 = set()
        block2 = set()
        block3 = set()

        for i in range(rows):
            rowSet = set()
            colSet = set()
            # every third row, clear the blocks
            if i % 3 == 0:
                block1 = set()
                block2 = set()
                block3 = set()
            for j in range(cols):
                # check row for duplicate numbers
                rowVal = blockVal = board[i][j]
                if rowVal in rowSet and rowVal != '.':
                    return False
                else:
                    rowSet.add(rowVal)

                # check column for duplicate numbers
                colVal = board[j][i]
                if colVal in colSet and colVal != '.':
                    return False
                else:
                    colSet.add(colVal)

                # check blocks for duplicate numbers
                if j < 3:
                    if blockVal in block1 and blockVal != '.':
                        return False
                    else:
                        block1.add(blockVal)
                elif j > 5:
                    if blockVal in block3 and blockVal != '.':
                        return False
                    else:
                        block3.add(blockVal)
                else:
                    if blockVal in block2 and blockVal != '.':
                        return False
                    else:
                        block2.add(blockVal)
        return True

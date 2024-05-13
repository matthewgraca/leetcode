from typing import List

class Solution:
    def __init__(self):
        pass

    # search target in row, then refine search for target in columns
    def searchMatrixRowThenCol(self, matrix: List[List[int]], target: int) -> bool:
        lenRows, lenCols = len(matrix), len(matrix[0])
        l, r = 0, lenRows-1

        # binary search for row containing target
        while l <= r:
            midRow = (l + r) // 2

            # if row contains the target, binary search for target 
            if target <= matrix[midRow][-1] and target >= matrix[midRow][0]:
                l, r = 0, lenCols-1
                while l <= r:
                    midCol = (l + r) // 2
                    if target < matrix[midRow][midCol]:
                        r = midCol-1
                    elif target > matrix[midRow][midCol]:
                        l = midCol+1
                    else:
                        return True
                # target not found in any column
                return False
                
            # target not contained in this row; determine if bianry search moves up or down
            if target < matrix[midRow][-1]:
                r = midRow-1
            else: # target > matrix[midRow][0]
                l = midRow+1
        # target not contained in any row
        return False

    # tricky indexing
    def searchMatrixRaw(self, matrix: List[List[int]], target: int) -> bool:
        lenRows, lenCols = len(matrix), len(matrix[0])
        l, r = 0, lenRows*lenCols-1
        while l <= r:
            mid = (r + l) // 2
            row, col = mid//lenCols, mid%lenCols
            if target > matrix[row][col]:
                l = mid+1
            elif target < matrix[row][col]:
                r = mid-1
            else:
                return True
        return False

from typing import List

class Solution:
    '''
    conditions for a valid sudoku:
    1. each row must contain the digits 1-9, no repeats
    2. each col must contain the digits 1-9, no repeats
    3. each 3x3 sub-box must contain the digits 1-9, no repitition

    So when I hear no repeats and the need to make a lot of comparisons, my
    mind really wants to use a set. My preliminary idea here is to use 3 sets;
    one that checks the row, one for the col, and a third for the sub-box

    So the idea here is to check each row, then each col, then each sub-box.
    Each row and each col will use a new set (potentially); the only tricky 
    thing here I see is the indexing for the sub-box, but I think that's possible 
    to formally define.

    First, let's start off with the easy stuff: row and col checking

    rows = 9
    cols = 9
    for i in range(rows):
        rowSet = set()
        colSet = set()
        for j in range(cols):
            rowVal = board[i][j]
            if rowVal in rowSet and rowVal != '.':
                return False
            else:
                rowSet.add(colVal)

            colVal = board[j][i]
            if colVal in colSet and colVal != '.':
                return False
            else:
                colSet.add(colVal)

    Second, is the tricky part where a 3x3 is invalid. At first glance this seems like 
    a tricky little indexing problem. Let's try to formalize this indexing, we'll start 
    with pseudocode:
    if (the row index is past the third, stop and move to next row)

    We want to avoid a situation where we retread steps; so in this case I think we 
    should use 3 sets, that way we can naturally follow how our loop iterates through 
    the 2d array.

    So, let's try:
    block1 = set()
    block2 = set()
    block3 = set()
    ...
    if col < 3
        add num to block1
    elseif col > 5
        add num to block3
    else
        add num to block2

    that checks every row at every third column; now we need to refresh the set 
    at every third row

    if row reaches a third, reset the set 
    '''
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

'''
Nothing really to say, I got this pretty much out of the gate. I noticed that 
there is a lot of searching and comparing for uniques, so set was my first idea. 
The only tricky thing here is indexing, which took quite a bit of time.

Time: n for scouring the array
    - O(n)
Space: less than 3n for the sets
    - O(n)
'''

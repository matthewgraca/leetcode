package solutions.arraysandhashing;

import java.util.HashSet;
/*
 * https://leetcode.com/problems/valid-sudoku/
 *
 * Complexity
 *  Let n be the size of the char board
 *  Time: O(n)
 *    O(n) for accessing the row set
 *    O(n) for accessing the column set
 *    O(n) for accessing the sub boards set
 *    O(2n) for accessing board row/col and col/row
 *  Space:  O(n)
 *    O(n/9) for the row set
 *    O(n/9) for the column set
 *    O(3n/9) for the sub boards sets
 */
public class ValidSudoku{
  public static boolean isValidSudoku(char[][] board){
    int n = board.length;
    // use 3 sub boards to track
    @SuppressWarnings("unchecked")  // we aren't doing bad things :)
    HashSet<Character>[] subBoards = new HashSet[n/3];
    for (int i = 0; i < subBoards.length; i++){
      subBoards[i] = new HashSet<Character>(n);
    }

    // increment through board
    for (int row = 0, subBoardRow = 0; row < n; row++, subBoardRow++){
      HashSet<Character> currentRow = new HashSet<>(n);
      HashSet<Character> currentCol = new HashSet<>(n);

      // clear up subboard if new ones are being checked
      if (subBoardRow == 3){
        subBoardRow = 0;
        for (HashSet<Character> sb : subBoards){
          sb.clear();
        }
      }

      for (int col = 0; col < n; col++){
        // check row
        char currentChar = board[row][col];
        if (currentChar != '.'){
          if (currentRow.contains(currentChar))
            return false;
          currentRow.add(currentChar);

          // check subboard
          int i = col / 3;
          if (!subBoards[i].add(currentChar))
            return false;
        }

        // check column
        currentChar = board[col][row];
        if (currentChar != '.'){
          if (currentCol.contains(currentChar))
            return false;
          currentCol.add(currentChar);
        }
      }
    }
    return true;
  }
}

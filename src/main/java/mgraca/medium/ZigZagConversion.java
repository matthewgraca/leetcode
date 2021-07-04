package mgraca.medium;
import java.util.Queue;
import java.util.LinkedList;
/*
 * Description: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
 *  rows like this:
 *  P   A   H   N
 *  A P L S I I G
 *  Y   I   R
 *  And then read line by line: "PAHNAPLSIIGYIR"
 *  Write the code that will take a string and make this conversion given a number of rows:
 *  string convert(string s, int numRows);
 *
 * Constraints:
 *  1 <= s.length <= 1000
 *  s consists of English letters (lower-case and upper-case), ',' and '.'.
 *  1 <= numRows <= 1000
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class ZigZagConversion{
  /*
   * Time/Space: O(n^2)
   */
  public static String convertV1(String s, int numRows){
    StringBuilder solution = new StringBuilder();
    if (numRows == 1){
      solution.append(s);
    }
    else{
      int n = s.length();
      char[][] charMatrix = new char[numRows][n];
      int i = 1;
      charMatrix[0][0] = s.charAt(0);
      // replicate the zigzag formation as a 2d array
      for (int col = 0; i < n; col++){
        // snake down
        if (col % 2 == 0){
          for (int row = 1; row < numRows && i < n; row++, i++){
            charMatrix[row][col] = s.charAt(i);  
          }
        }
        // snake up
        else{
          for (int row = numRows - 2; row >= 0 && i < n; row--, i++){
            charMatrix[row][col] = s.charAt(i);
          }
        }
      }
      // append the solution string
      for (int row = 0; row < numRows; row++){
        for (int col = 0; col < n; col++){
          if (charMatrix[row][col] != '\u0000'){
            solution.append(charMatrix[row][col]);
          }
        }
      }
    }
    return solution.toString();
  }

  /*
   * Time/Space: O(n)
   */
  public static String convertV2(String s, int numRows){
    StringBuilder solution = new StringBuilder();
    if (numRows == 1){
      solution.append(s);
    }
    else{
      int n = s.length();
      // create an array of queues
      Queue<Character>[] charMatrix = new Queue[numRows];
      for (int j = 0; j < numRows; j++){
        charMatrix[j] = new LinkedList<Character>();
      }
      int i = 0;
      // replicate the zigzag formation like a 2d array
      for (int col = 0; i < n; col++){
        // snake down
        if (col % 2 == 0){
          for (int row = 0; row < numRows - 1 && i < n; row++, i++){
            charMatrix[row].add(s.charAt(i));
          }
        }
        // snake up
        else{
          for (int row = numRows - 1; row > 0 && i < n; row--, i++){
            charMatrix[row].add(s.charAt(i));
          }
        }
      }
      // construct the solution string
      for (int row = 0; row < numRows; row++){
        while(!charMatrix[row].isEmpty()){
          solution.append(charMatrix[row].remove());
        }
      }
    }
    return solution.toString();
  }
}

package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.arraysandhashing.ValidSudoku.isValidSudoku;

import java.util.Arrays;
public class ValidSudokuTest{
  @Test
  public void example1(){
    char[][] input = {
        {'5','3','.','.','7','.','.','.','.'}
        ,{'6','.','.','1','9','5','.','.','.'}
        ,{'.','9','8','.','.','.','.','6','.'}
        ,{'8','.','.','.','6','.','.','.','3'}
        ,{'4','.','.','8','.','3','.','.','1'}
        ,{'7','.','.','.','2','.','.','.','6'}
        ,{'.','6','.','.','.','.','2','8','.'}
        ,{'.','.','.','4','1','9','.','.','5'}
        ,{'.','.','.','.','8','.','.','7','9'}
      };
    //System.out.println(Arrays.deepToString(input).replace('], [', '],\n ['));
    boolean expected = true;
    boolean actual = isValidSudoku(input);
    assertTrue(expected == actual);
  }

  @Test
  public void invalidSubBoard(){
    char[][] input = {
        {'8','3','.','.','7','.','.','.','.'}
        ,{'6','.','.','1','9','5','.','.','.'}
        ,{'.','9','8','.','.','.','.','6','.'}
        ,{'8','.','.','.','6','.','.','.','3'}
        ,{'4','.','.','8','.','3','.','.','1'}
        ,{'7','.','.','.','2','.','.','.','6'}
        ,{'.','6','.','.','.','.','2','8','.'}
        ,{'.','.','.','4','1','9','.','.','5'}
        ,{'.','.','.','.','8','.','.','7','9'}
      };
    boolean expected = false;
    boolean actual = isValidSudoku(input);
    assertTrue(expected == actual);
  }

  @Test
  public void twoOnSameRow(){
    char[][] input = {
        {'5','3','.','.','5','.','.','.','.'}
        ,{'6','.','.','1','9','5','.','.','.'}
        ,{'.','9','8','.','.','.','.','6','.'}
        ,{'8','.','.','.','6','.','.','.','3'}
        ,{'4','.','.','8','.','3','.','.','1'}
        ,{'7','.','.','.','2','.','.','.','6'}
        ,{'.','6','.','.','.','.','2','8','.'}
        ,{'.','.','.','4','1','9','.','.','5'}
        ,{'.','.','.','.','8','.','.','7','9'}
      };
    boolean expected = false;
    boolean actual = isValidSudoku(input);
    assertTrue(expected == actual);
  }

  @Test
  public void twoOnSameCol(){
    char[][] input = {
        {'5','3','.','.','7','.','.','.','9'}
        ,{'6','.','.','1','9','5','.','.','.'}
        ,{'.','9','8','.','.','.','.','6','.'}
        ,{'8','.','.','.','6','.','.','.','3'}
        ,{'4','.','.','8','.','3','.','.','1'}
        ,{'7','.','.','.','2','.','.','.','6'}
        ,{'.','6','.','.','.','.','2','8','.'}
        ,{'.','.','.','4','1','9','.','.','5'}
        ,{'.','.','.','.','8','.','.','7','9'}
      };
    boolean expected = false;
    boolean actual = isValidSudoku(input);
    assertTrue(expected == actual);
  }

  @Test
  public void example3(){
    char[][] input = {
         {'.','.','.','.','.','.','.','.','.'}
        ,{'4','.','.','.','.','.','.','.','.'}
        ,{'.','.','.','.','.','.','6','.','.'}
        ,{'.','.','.','3','8','.','.','.','.'}
        ,{'.','5','.','.','.','6','.','.','1'}
        ,{'8','.','.','.','.','.','.','6','.'}
        ,{'.','.','.','.','.','.','.','.','.'}
        ,{'.','.','7','.','9','.','.','.','.'}
        ,{'.','.','.','6','.','.','.','.','.'}
      };
    boolean expected = true;
    boolean actual = isValidSudoku(input);
    assertTrue(expected == actual);
  }
}

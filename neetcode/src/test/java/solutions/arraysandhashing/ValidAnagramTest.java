package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class ValidAnagramTest{
  @Test
  public void example1(){
    String input1 = "anagram";
    String input2 = "nagaram";
    boolean expected = true;
    boolean actual = ValidAnagram.isAnagram(input1, input2);
    assertTrue(expected == actual);
  }

  @Test
  public void example2(){
    String input1 = "rat";
    String input2 = "car";
    boolean expected = false;
    boolean actual = ValidAnagram.isAnagram(input1, input2);
    assertTrue(expected == actual);
  }

  @Test
  public void example3(){
    String input1 = "aacc";
    String input2 = "ccac";
    boolean expected = false;
    boolean actual = ValidAnagram.isAnagram(input1, input2);
    assertTrue(expected == actual);
  }
}

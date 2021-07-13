package mgraca.hard;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class RegularExpressionMatchingTest{
  //@Test
  public void example1(){
    assertTrue(RegularExpressionMatching.isMatch("aa", "a") == false);
  }

  //@Test
  public void example2(){
    assertTrue(RegularExpressionMatching.isMatch("aa", "a*") == true);
  }

  //@Test
  public void example3(){
    assertTrue(RegularExpressionMatching.isMatch("ab", ".*") == true);
  }

  //@Test
  public void example4(){
    assertTrue(RegularExpressionMatching.isMatch("aab", "c*a*b") == true);
  }

  //@Test
  public void example5(){
    assertTrue(RegularExpressionMatching.isMatch("mississippi", "mis*is*p*") == false);
  }
}

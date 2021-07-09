package mgraca.hard;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class RegularExpressionMatchingTest{
  @Test
  public void example1(){
    assertTrue(RegularExpressionMatching.isMatch("", "") == false);
  }
}

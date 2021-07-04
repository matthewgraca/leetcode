package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ZigZagConversionTest{
  @Test
  public void example1(){
    assertTrue(ZigZagConversion.convert("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR"));
  }

  @Test
  public void example2(){
    assertTrue(ZigZagConversion.convert("PAYPALISHIRING", 4).equals("PINALSIGYAHRPI"));
  }

  @Test
  public void example3(){
    assertTrue(ZigZagConversion.convert("A", 1).equals("A"));
  }

  @Test
  public void example4(){
    assertTrue(ZigZagConversion.convert("AB", 1).equals("AB"));
  }
}

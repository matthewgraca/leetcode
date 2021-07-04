package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ZigZagConversionTest{
  @Test
  public void example1V1(){
    assertTrue(ZigZagConversion.convertV1("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR"));
  }

  @Test
  public void example2V1(){
    assertTrue(ZigZagConversion.convertV1("PAYPALISHIRING", 4).equals("PINALSIGYAHRPI"));
  }

  @Test
  public void example3V1(){
    assertTrue(ZigZagConversion.convertV1("A", 1).equals("A"));
  }

  @Test
  public void example4V1(){
    assertTrue(ZigZagConversion.convertV1("AB", 1).equals("AB"));
  }

  @Test
  public void example1V2(){
    assertTrue(ZigZagConversion.convertV2("PAYPALISHIRING", 3).equals("PAHNAPLSIIGYIR"));
  }

  @Test
  public void example2V2(){
    assertTrue(ZigZagConversion.convertV2("PAYPALISHIRING", 4).equals("PINALSIGYAHRPI"));
  }

  @Test
  public void example3V2(){
    assertTrue(ZigZagConversion.convertV2("A", 1).equals("A"));
  }

  @Test
  public void example4V2(){
    assertTrue(ZigZagConversion.convertV2("AB", 1).equals("AB"));
  }
}

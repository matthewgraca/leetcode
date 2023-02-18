package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ReverseIntegerTest{
  @Test
  public void exampleSlow1(){
    assertTrue(ReverseInteger.reverseSlow(123) == 321);
  }

  @Test
  public void exampleSlow2(){
    assertTrue(ReverseInteger.reverseSlow(-123) == -321);
  }

  @Test
  public void exampleSlow3(){
    assertTrue(ReverseInteger.reverseSlow(120) == 21);
  }

  @Test
  public void exampleSlow4(){
    assertTrue(ReverseInteger.reverseSlow(0) == 0);
  }

  @Test
  public void exampleSlow5(){
    assertTrue(ReverseInteger.reverseSlow(1000000003) == 0);
  }

  @Test
  public void exampleSlow6(){
    assertTrue(ReverseInteger.reverseSlow(-1000000003) == 0);
  }

  @Test
  public void exampleFast1(){
    assertTrue(ReverseInteger.reverseFast(123) == 321);
  }

  @Test
  public void exampleFast2(){
    assertTrue(ReverseInteger.reverseFast(-123) == -321);
  }

  @Test
  public void exampleFast3(){
    assertTrue(ReverseInteger.reverseFast(120) == 21);
  }

  @Test
  public void exampleFast4(){
    assertTrue(ReverseInteger.reverseFast(0) == 0);
  }

  @Test
  public void exampleFast5(){
    // overflows to negative
    assertTrue(ReverseInteger.reverseFast(1000000003) == 0);
  }

  @Test
  public void exampleFast6(){
    assertTrue(ReverseInteger.reverseFast(-1000000003) == 0);
  }

  @Test
  public void exampleFast7(){
    // overflows to positive
    assertTrue(ReverseInteger.reverseFast(1000000005) == 0);
  }
}

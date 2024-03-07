package solutions.slidingwindow;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.slidingwindow.BestTimeToBuyAndSellStock.maxProfit;

public class BestTimeToBuyAndSellStockTest{
  @Test
  public void example1(){
    int[] input = {7,1,5,3,6,4};
    int expected = 5;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example2(){
    int[] input = {7,6,4,3,1};
    int expected = 0;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example3(){
    int[] input = {7,1,100,3,6,4};
    int expected = 99;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example4(){
    int[] input = {7,2,3,1,100,3,6,4};
    int expected = 99;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example5(){
    int[] input = {1};
    int expected = 0;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example6(){
    int[] input = {2,1};
    int expected = 0;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example7(){
    int[] input = {2,1,2,0,1};
    int expected = 1;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example8(){
    int[] input = {2,1,2,1,0,1,2};
    int expected = 2;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example9(){
    int[] input = {3,3,5,0,0,3,1,4};
    int expected = 4;
    int actual = maxProfit(input);

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }
}

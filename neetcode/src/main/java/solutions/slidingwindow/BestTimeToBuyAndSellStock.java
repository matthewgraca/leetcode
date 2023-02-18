package solutions.slidingwindow;

/*
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * Complexity
 *  Time:
 *  Space:
 */
public class BestTimeToBuyAndSellStock{
  public static int maxProfit(int[] prices){
    int left = 0;
    int right = 1;
    int maxProfit = 0;
    while (right < prices.length){
      // finds new minimum, keeping left < right pointer
      if (prices[left] < prices[right]){
        maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
        right++;
      }
      else{ // if new min is found, push up window
        left = right;
        right++;
      }
    }
    return maxProfit;
  }

  public static int slowMaxProfit(int[] prices){
    int maxProfit = 0;
    for (int i = 0; i < prices.length-1; i++){
      int currentPrice = prices[i];
      for (int j = i+1; j < prices.length; j++){
        int futurePrice = prices[j];
        int currentProfit = futurePrice - currentPrice;
        if (currentProfit > maxProfit){
          maxProfit = currentProfit;
        }
      }
    }
    return maxProfit;
  }
}

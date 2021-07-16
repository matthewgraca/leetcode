package mgraca.medium;

/*
 * Description: Given an integer, convert it to a roman numeral.
 *
 * Constraints:
 *  1 <= num <= 3999
 * 
 * Complexity:
 *  Let n be the number of digits in num
 *  Time:   O(n)
 *  Space:  O(n)
 */
public class IntegerToRoman{
  public static String intToRoman(int num){
    String[] thousands = new String[]{"M", "MM", "MMM"};
    String[] hundreds = new String[]{"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    String[] tens = new String[]{"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String[] ones = new String[]{"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    String solution = "";

    if (num / 1000 > 0){
      solution = solution.concat(thousands[num / 1000 - 1]);
      num = num % 1000;
    }
    if (num / 100 > 0){
      solution = solution.concat(hundreds[num / 100 - 1]);
      num = num % 100;
    }
    if (num / 10 > 0){
      solution = solution.concat(tens[num / 10 - 1]);
      num = num % 10;
    }
    if (num > 0){
      solution = solution.concat(ones[num - 1]);
    }
    return solution;
  }
}

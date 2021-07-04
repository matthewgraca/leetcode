package mgraca.easy;

/*
 * Description: Given a signed 32-bit integer x, return x with its digits reversed. 
 *  If reversing x causes the value to go outside the signed 32-bit integer range 
 *  [-2^(31), 2^(31) - 1], then return 0.
 *  Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
 *
 * Constraints:
 *  -2^(31) <= x <= 2^(31) - 1
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class ReverseInteger{
  public static int reverseSlow(int x){
    // reverse the string representation of the integer
    int solutionInt = 0;
    StringBuilder solution = new StringBuilder(String.valueOf(x));
    solution.reverse();

    // handle the - character when x < 0, and prevent under/overflow
    if (x < 0){
      solution.deleteCharAt(solution.length()-1);
      solution.insert(0, '-');
    }

    // parse solution string; return 0 if over/underflow detected
    try{
      solutionInt = Integer.parseInt(solution.toString());
    }
    catch(NumberFormatException e){
      solutionInt = 0;
    }
    return solutionInt; 
  }

  public static int reverseFast(int x){
    return 0;
  }
}

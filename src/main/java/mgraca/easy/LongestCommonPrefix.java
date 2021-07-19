package mgraca.easy;

/*
 * Description: Write a function to find the longest common prefix string amongst an array of
 *  strings.
 *  If there is no common prefix, return an empty string "".
 *
 * Constraints:
 *  1 <= strs.length <= 200
 *  0 <= strs[i].length <= 200
 *  strs[i] consists of only lower-case English letters.
 * 
 * Complexity:
 *  Time:
 *  Space:
 */
public class LongestCommonPrefix{
  public static String naiveLongestCommonPrefix(String[] strs){
    String solution = "";
    if (strs.length == 1){
      solution = strs[0];
    }
    else{
      int i = 0, j = 0;
      boolean contScan = true;
      // scan the words
      while (contScan && i+1 < strs.length){
        // compare the letter in this word to the letter in the word next to it
        if (j < strs[i].length() && j < strs[i+1].length() && 
            strs[i].charAt(j) == strs[i+1].charAt(j)){
          i++;
        }
        else{
          contScan = false;
        }
        // if the letter has been scanned on all words, check next letter
        if (i+1 == strs.length && contScan){
          solution = solution + strs[i].charAt(j);
          i = 0;
          j++;
        }
      }
    }
    return solution;
  }

  public static String fastLongestCommonPrefix(String[] strs){
    return "";
  }
}

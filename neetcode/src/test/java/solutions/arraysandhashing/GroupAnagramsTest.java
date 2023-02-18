package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.arraysandhashing.GroupAnagrams.groupAnagrams;

import java.util.List;
import java.util.Arrays;
import java.util.Collections;

public class GroupAnagramsTest{
  @Test
  public void example1(){
    // initialize
    String[] input = {"eat","tea","tan","ate","nat","bat"};
    List<List<String>> expected = Arrays.asList(Arrays.asList("bat"), 
                                                Arrays.asList("nat","tan"), 
                                                Arrays.asList("ate","eat","tea"));
    List<List<String>> actual = groupAnagrams(input);
    // ignore order of expected
    for (int i = 0; i < expected.size(); i++){
      Collections.sort(expected.get(i));
    }
    Collections.sort(expected, (a,b) -> a.get(0).compareTo(b.get(0)));
    // ignore order of actual
    for (int i = 0; i < actual.size(); i++){
      Collections.sort(actual.get(i));
    }
    Collections.sort(actual, (a,b) -> a.get(0).compareTo(b.get(0)));
    
    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.equals(expected));
  }

  @Test
  public void example2(){
    // initialize
    String[] input = {""};
    List<List<String>> expected = Arrays.asList(Arrays.asList(""));
    List<List<String>> actual = groupAnagrams(input);
    // ignore order of expected
    for (int i = 0; i < expected.size(); i++){
      Collections.sort(expected.get(i));
    }
    Collections.sort(expected, (a,b) -> a.get(0).compareTo(b.get(0)));
    // ignore order of actual
    for (int i = 0; i < actual.size(); i++){
      Collections.sort(actual.get(i));
    }
    Collections.sort(actual, (a,b) -> a.get(0).compareTo(b.get(0)));
 
    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.equals(expected));
  }

  @Test
  public void example3(){
    // initialize
    String[] input = {"a"};
    List<List<String>> expected = Arrays.asList(Arrays.asList("a"));
    List<List<String>> actual = groupAnagrams(input);
    // ignore order of expected
    for (int i = 0; i < expected.size(); i++){
      Collections.sort(expected.get(i));
    }
    Collections.sort(expected, (a,b) -> a.get(0).compareTo(b.get(0)));
    // ignore order of actual
    for (int i = 0; i < actual.size(); i++){
      Collections.sort(actual.get(i));
    }
    Collections.sort(actual, (a,b) -> a.get(0).compareTo(b.get(0)));
 
    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.equals(expected));
  }
}

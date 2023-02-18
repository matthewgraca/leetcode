package solutions.arraysandhashing;

import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.Map;
import java.util.AbstractMap.SimpleImmutableEntry;
/*
 * https://leetcode.com/problems/top-k-frequent-elements/
 *
 * Complexity
 *  Time:
 *
 *  Space:
 */
public class TopKFrequentElements{

  // same as solution 1, but instead of switching key-value, we just tell the
  //  max heap comparator to add to the heap based off of value, not key
  public static int[] topKFrequent(int[] nums, int k){
    // count instances of each value in nums using a map
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums){
      if (!map.containsKey(num))
        map.put(num, 0);
      map.put(num, map.get(num)+1);
    }

    // create max heap, but enqueue based off of count value instead of key
    PriorityQueue<Map.Entry<Integer, Integer>> pq =
      new PriorityQueue<>((a,b)->b.getValue()-a.getValue());
    for (Map.Entry<Integer, Integer> hm : map.entrySet()){
      pq.add(hm);
    }

    // create solution
    int[] solution = new int[k];
    for (int i = 0; i < k; i++){
      solution[i] = pq.poll().getKey();
    }
    return solution;
  }

  /*
   *  solution 2:
   *  O(n) - to create the hashmap
   *  O(k*n) - to find the maxes
   *  O(k) - to create the solution
   *
   *  O(kn) - looks more attractive, but for large k it's much worse performance
   *    -if n is all distinct, and k = n, we're looking at O(n^2), basically
   *    just selection sorting at that point
   */
  public static int[] solution2(int[] nums, int k){
    // count instances of each value in nums using a map
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums){
      if (!map.containsKey(num))
        map.put(num, 0);
      map.put(num, map.get(num)+1);
    }

    // find the max at each iteration from 0->k
    int[] solution = new int[k];
    for (int i = 0; i < k; i++){
      int max = Integer.MIN_VALUE;
      int key = Integer.MIN_VALUE;
      for (Map.Entry<Integer, Integer> hm : map.entrySet()){
        if (hm.getValue() > max){
          max = hm.getValue();
          key = hm.getKey();
        }
      }
      solution[i] = key;
      map.remove(key);
    }
    return solution;
  }

  /*
   *  solution 1:
   *  O(n) - to create the hashmap
   *  O(nlogn) - to create the priority queue
   *  O(k) - to create the solution
   *
   *  O(n + nlogn + k) = O(nlogn + k)
   *    -if n is distinct with k approaching n, we have O(nlogn)
   */
  public static int[] solution1(int[] nums, int k){
    // count instances of each value in nums using a map
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums){
      if (!map.containsKey(num))
        map.put(num, 0);
      map.put(num, map.get(num)+1);
    }


    // reverse key-val pairs, but in a heap so it's ordered by val
    // java giga-bs: SIE allows one key-value pair to be defined (can't use size 1 hashmap)
    // lambda expression enables pq to be a max heap instead of the default min heap    
    PriorityQueue<SimpleImmutableEntry<Integer, Integer>> pq = 
      new PriorityQueue<>((a,b) -> b.getKey()-a.getKey());
    for (Map.Entry<Integer, Integer> hm : map.entrySet()){
      SimpleImmutableEntry<Integer, Integer> entry = 
        new SimpleImmutableEntry<>(hm.getValue(), hm.getKey());
      pq.add(entry);
    }

    // generate solution
    int[] solution = new int[k];
    for (int i = 0; i < k; i++){
      int item = pq.poll().getValue();
      solution[i] = item;
    }
    return solution;
  }
}

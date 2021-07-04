# Longest Substring Without Repeating Characters
## Sliding Window
<p>This implementation uses a method called the "sliding window". This approach generally scans an array by forming a "window" around a group of contiguous elements. This comes in handy when you need to check the next element in an array, but may need to discard previous elements based off of what the next element is.</p>
<p>As a discrete example, find the largest sum of 5 consecutive numbers in an array of integers, of size 20.</p>
<p>The naive approach would have you sum every element from a[0] to a[4], then a[1] to a[5], then a[2] to a[6], etc., and compare those sums to the current max sum.</p>
<img src="https://i.stack.imgur.com/2Dneo.png" alt="naive_solution">
<p>  However, by utilizing the sliding window and the observation that you are summing numbers you've already summed, what you can do is:</p>
<ul>
  <li>Sum a[0] to a[4]</li>
  <li>Subtract a[0], add a[5], compare sums</li>
  <li>Subtract a[1], add a[6], compare sums</li>
  <li>etc...</li>
</ul>
<img src="https://i.stack.imgur.com/zsGl7.png" alt="sliding-window">
<p>This way, you aren't summing the same numbers over and over again; and as you iterate through the array, you are moving the left window and the right window that constitute the indeces of the array.</p>

<p>For more information and a fantastic visual example, see <a href="https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples/64111403#64111403">this</a>.</p>

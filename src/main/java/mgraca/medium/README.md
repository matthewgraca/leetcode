# Longest Substring Without Repeating Characters
This implementation uses a method called the "sliding window". This approach generally scans an array by forming a "window" around a group of contiguous elements. This comes in handy when you need to check the next element in an array, but may need to discard previous elements based off of what the next element is.
The classic example is finding the sum of x number of consecutive elements of an array of size n.
The naive approach would have you sum the elements from 0 to x, then 1 to x+1, then 2 to x+2, etc.
However, by utilizing the sliding window and the observation that you are summing numbers you've already summed, what you can do is:
  Sum 0 to x
  Subtract 0, add x+1
  Subtract 2, add x+2
  etc...
This way, you aren't summing the same numbers over and over again; and as you iterate through the array, you are moving the left window and the right window that constitute the indeces of the array.

For more information and a fantastic visual example, see <a href="https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples/64111403#64111403">this</a>.

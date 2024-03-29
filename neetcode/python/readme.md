# commands and stuff
## run unit tests:
```bash
python3 -m unittest -v \path\to\your\test\file\:3
```
## patterns
### arrays and hashing
- If you do a TON of comparing and searching, hashing should be your first thought

### two pointers
- Whenever you think that you need to do a scan of an array that is n^2, think if you can do it in n time with two pointers. 

### sliding window
- Pretty much the same as two pointers, but instead it's about evaluating items in a window of an array
- It's here that we see a lot of frequency maps (maps that count the number of characters in a string)
- The last problem had a wacky monotonically decreasing deque -- I'll be honest, I don't see the vision for when you'd need that. It's almost like a heap, but using one side to track the max and the other side to add "potentially max" values, in this case. It's almost dynamic progamming-esque, the way it discards overlapping subproblems.

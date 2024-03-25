'''
My initial idea here is to scan forward in the array. As we scan, 
we pick up characters; if we end up picking up a duplicate character, 
we save the length of that substring and restart the scan from that duplicate.

The only concern I have is that checking if the character is contained in the 
substring may get expensive; if the string has all unique characters, then 
I think it'll be n(n-1)/2 compares in the substring, or n^2.

If this is not performant, I think a set would come in handy here, since 
seaching and preventing duplicates is super efficient

...

One issue is that in strings like "dvdf", my algorithm checks "dv", sees 
"d", then checks "df" when it should check "vdf". So we need a way to 
"return" to the character that's not a duplicate. I see why this will 
require two pointers.

...

Okay, I solved the problem -- but I feel like there's a really easy 
optimization here that I can use with a set instead of string comparision.

Let's make a set that contains all the characters currently contained in 
substr, and simply use that for comparison instead.

Time: n to traverse the array. n^2 to create the substring if every character 
in the array is distinct (n(n-1)/2 compares, which is somehow just as expensive
as the set solution with n compares, idk lol. I guess because generating the 
substring is itself n(n-1)/2, and what bottlenecks?)

I just realized here that I can forget about generating the substring; just 
keep the set -- only like a 10% time improvement, but better than just 1ms.
'''
class Solution:
    '''
    def lengthOfLongestSubstring(s: str) -> int:
        maxSLength = 0
        substr = ""
        l, r = 0, 0
        while r < len(s):
            while s[r] in substr:
                l += 1
                substr = s[l:r]
            substr += s[r]
            r += 1
            maxSLength = max(maxSLength,len(substr))
        return maxSLength
    '''
    def lengthOfLongestSubstring(s: str) -> int:
        maxSLength = 0
        strSet = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            strSet.add(s[r])
            r += 1
            maxSLength = max(maxSLength,len(strSet))
        return maxSLength
'''
Seems like sliding window really lends itself to substring work. By the way, 
aren't all sliding window problems just two pointer problems? I guess the diff 
is that in sliding window, we care about what's inside the window, while for 
two pointer we don't necessarily care after passing through?

Time: n to traverse the array, n compares made with the set
    - O(n)
Space: n to create the set
    - O(n)
'''

from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def __init__(self):
        pass

    def ladderLength(self, 
        beginWord: str, 
        endWord: str, 
        wordList: List[str]
    ) -> int:
        # create an adjaceny list between the words in the list
        # include the beginning word as well
        wordList.append(beginWord)
        adj = defaultdict(list) 
        for word in wordList:
            for j in range(len(word)):
                # instead of mapping words different by one letter as adjacent, 
                # map the generic pattern adjacent to the word
                # e.g. *ot: hot, h*t: hot, ho*: hot; etc...
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)

        # adj maps patterns to words, so if the end word isn't in the list,
        # we need to exclude now because bfs assumes it exists
        if endWord not in wordList:
            return 0

        # search from the end word to the beginning word
        return self.bfs(adj, endWord, beginWord)
        
    def bfs(self, adj: dict, start: str, end: str) -> int:
        count = 1
        visited = set([start])
        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return count
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in adj[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            count += 1

        # not found
        return 0 
'''
goal: find all the words that differ from the starting
word by only one letter.

each word has a counter. we check letter by letter.
if the word has the same letter in the same position as 
beginWord, we increment the counter. we pick the character that
has a counter of len(beginWord) - 1

are we building an adjaceny list?
then we run bfs on the list?

[hot, dot], [hot, lot], [dot, dog], [dog, log], [dog, cog]


so the solution turned out to be my initial intuition, backwards.
instead of mapping words to patterns, we map patterns to words:
    e.g. *ot : hot, dot, lot

we do this by grabbing the word; for every index i, we "generalize"
the word by removing a letter and replacing it with a "*", then add it
to the map where the pattern maps to the word. doing this for every word, 
we make generalized patterns for every word in the list.
    - so for a word of m size, there are n*m patterns

then to perform bfs, we take the word, generalize it to the pattern, then look at its neighbors.
we do bfs backwards from the target to the source, so it's guarnteed to be the shortest solution.
e.g. begin with hit, end with cog
    - search from cog
    - look for *og (log, dog), c*g (none), co* (none)
    - looking from log and dog:
        - use patterns: l*g, lo* and d*g, do* 
    etc. until start word is found

time:
    - adj map: n + 1 words with length m: each word generates m paths; so takes O(nm) time to make the adj map
    - check for endWord in words: O(n)
    - bfs on the adj map: worst case the word is a leaf on the rightmost; takes O(nm) time
total: O(nm)

compared to my solution, which i think got bottlenecked at the adj map generation:
    O(n^2). since m <= 10 and n <= 5000, this is two orders of magnitude worse.
'''

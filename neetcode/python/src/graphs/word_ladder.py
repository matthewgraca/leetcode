from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def __init__(self):
        pass

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # adjacency list where a pattern is adjacent to the word that matches the pattern
        # i.e. "pattern" describes a family of words that are adjacent to each other
        # e.g. "*ot : [hot, cot, pot, lot]"; under "*ot", "hot" and "cot" are adjacent ...
        # ... but under "h*t", they would not be adjacent
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + "*" + word[i + 1 :]
                adj[pattern].append(word)
        
        # run bfs for shortest path
        count = 1
        q = deque([beginWord])
        visit = set([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                # convert word into all possible patterns, 
                # then investigate all adjacent words
                for i in range(len(word)):
                    pattern = word[: i] + "*" + word[i + 1 :]
                    for adjWord in adj[pattern]:
                        if adjWord not in visit:
                            q.append(adjWord)
                            visit.add(adjWord)
            count += 1
        
        # no path to end word or end word dne
        return 0

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # char: TrieNode
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

class Solution:
    def __init__(self):
        pass

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create trie of the search keys
        root = TrieNode()
        for word in words:
            root.addWord(word)

        # check every path starting from (i,j)
        res = []
        rows, cols  = len(board), len(board[0])
        for row in range(0, rows):
            for col in range(0, cols):
                self.checkNode(board, [], root, row, col, res)
        return res 

    # checks if a path starting from x,y is valid
    def checkNode(
        self,
        board: List[List[int]],
        word: List[str],
        trieNode: TrieNode,
        x: int,
        y: int,
        res: set()
    ) -> bool:
        # if node is not valid, backtrack
        if not self.validNode(board, trieNode, x, y):
            return

        # check curr node
        visitedNode = board[x][y]
        board[x][y] = "" # mark node as visited
        trieNode = trieNode.children[visitedNode]
        word.append(visitedNode)
        if trieNode.endOfWord:
            res.append("".join(word))
            trieNode.endOfWord = False

        # check neighbors
        # right, down, left, up
        self.checkNode(board, word, trieNode, x+1, y, res) 
        self.checkNode(board, word, trieNode, x, y+1, res) 
        self.checkNode(board, word, trieNode, x-1, y, res) 
        self.checkNode(board, word, trieNode, x, y-1, res) 

        # path from x,y failed; backtrack and unvisit nodes
        word.pop()
        board[x][y] = visitedNode

        # invalid node or no solution; backtrack
        return 

    # determine if a node is valid:
    # x,y is in bounds and letter is in the trie
    def validNode(
        self, 
        board: List[List[int]], 
        trieNode: TrieNode,
        x: int, 
        y: int
    ) -> bool:
        m, n = len(board), len(board[0])
        return(
            x < m and y < n and x >= 0 and y >= 0 and 
            board[x][y] in trieNode.children
        )

'''
The best way i can describe this is this is the word search backtracking problem, 
but we change the conditions for what makes a success/fail that requires a backtrack

we search the matrix in tandem with a trie of the search keys.

if the word is in the trie, we append to the solution
if the word is not in the trie, we backtrack the matrix dfs 
'''

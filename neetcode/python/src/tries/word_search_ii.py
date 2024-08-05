from typing import List

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

        return

    def removeWord(self, word: str) -> None:
	    # get the path of the word in the trie
        curr = self
        nodeStack = []
        for char in word:
            nodeStack.append((curr, char))
            curr = curr.children[char]
	    # remove the nodes from the trie if they're childless
	    # if they have children, exit; this path needs to exist for other keys
        while nodeStack:
            parentNode, char = nodeStack.pop()
            childNode = parentNode.children[char]
            if not childNode.children:
                del parentNode.children[char]
            else:
                return

        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # put search keys in words into a trie
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        # run dfs on matrix in parallel with trie to search
        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(root, root, board, "", row, col, set(), res)
        
        return res

    def dfs(
        self,
        root: TrieNode, 
        node: TrieNode,
        board: List[List[str]], 
        word: str, 
        row: int,
        col: int,
        visited: set,
        res: List[str]
    ) -> None:
        # key scan finished; word found
        if node.endOfWord:
            res.append(word)
            node.endOfWord = False
            root.removeWord(word)
            # don't return; there may be more words on this path

        # current node not promising; backtrack
        if not self.promising(node, board, row, col, visited):
            return

        # traverse trie in parallel with matrix dfs
        visited.add((row, col))
        word += board[row][col]
        node = node.children[board[row][col]]

        # dfs
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            self.dfs(root, node, board, word, r, c, visited, res)
        visited.remove((row, col))

        return

    def promising(
        self,
        node: TrieNode,
        board: List[List[int]],
        row: int,
        col: int,
        visited: set
    ) -> bool:
        return (
            row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and
            (row, col) not in visited and
            board[row][col] in node.children
        )

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        return 

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, curr: TrieNode, word: str, i: int) -> bool:
        # scan of search key finished; check if it is a valid word in the trie
        if i >= len(word):
            return curr.endOfWord

        # if wildcard, check all children
        if word[i] == ".":
            for child in curr.children.values():
                if self.dfs(child, word, i + 1):
                    return True
        # if regular character, normally traverse
        elif word[i] in curr.children:
            if self.dfs(curr.children[word[i]], word, i + 1):
                return True
        # not a wildcard and char not in trie
        else:
            return False
        
        # dfs failed on children
        return False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        
        curr.isWord = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res = []
        def backtrack(i, j, node, word):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == ' ' or board[i][j] not in node.children:
                return

            c = board[i][j]
            node = node.children[c]
            word += c

            if node.isWord:
                res.append(word)
                node.isWord = False

            tmp = board[i][j]
            board[i][j] = ' '

            backtrack(i+1, j, node, word)
            backtrack(i-1, j, node, word)
            backtrack(i, j+1, node, word)
            backtrack(i, j-1, node, word)

            board[i][j] = tmp

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, root, "")


        return res
# Word Ladder I
# https://www.interviewbit.com/problems/word-ladder-i/
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#
#         You must change exactly one character in every transformation
#         Each intermediate word must exist in the dictionary
#
# Example :
#
# Given:
#
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
#
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note that we account for the length of the transformation path instead of the number of transformation itself.
#
#     Note:
#
#         Return 0 if there is no such transformation sequence.
#         All words have the same length.
#         All words contain only lowercase alphabetic characters.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class TrieNode:
        def __init__(self):
            self.chars = dict()
            self.word = False
            self.marker = False

        def insertWord(self, word):
            current = self
            for char in word:
                if char not in current.chars:
                    current.chars[char] = Solution.TrieNode()
                current = current.chars[char]
            current.word = True

        def findWord(self, word):
            tmp = self
            for char in word:
                if char not in tmp.chars:
                    return None
                tmp = tmp.chars[char]
            return tmp

    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque
        from string import ascii_lowercase

        trie, queue = Solution.TrieNode(), deque()
        for i, word in enumerate(wordList):
            trie.insertWord(word)

        queue.append((beginWord, 1))

        while len(queue) > 0:
            word, dist = queue.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for c in ascii_lowercase:
                    if word[i] == c:
                        continue
                    new_word = word[:i] + c + word[i + 1:]

                    node = trie.findWord(new_word)
                    if node and not node.marker:
                        node.marker = True
                        queue.append((new_word, dist + 1))

        return 0
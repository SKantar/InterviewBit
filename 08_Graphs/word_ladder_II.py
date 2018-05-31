# Word Ladder II
# https://www.interviewbit.com/problems/word-ladder-ii/
#
# Given two words (start and end), and a dictionary, find the shortest transformation sequence
# from start to end, such that:
#
#         Only one letter can be changed at a time
#         Each intermediate word must exist in the dictionary
#
# If there are multiple such sequence of shortest length, return all of them. Refer to the example
# for more details.
#
# Example :
#
# Given:
#
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
#
# Return
#
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
#
#     Note:
#
#         All words have the same length.
#         All words contain only lowercase alphabetic characters.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class TrieNode:
        def __init__(self):
            self.chars = dict()
            self.idx = None
            self.dist = 0

        def insertWord(self, i, word, dist=-1):
            current = self
            for char in word:
                if char not in current.chars:
                    current.chars[char] = Solution.TrieNode()
                current = current.chars[char]
            current.idx = i
            current.dist = dist

        def findWord(self, word):
            tmp = self
            for char in word:
                if char not in tmp.chars:
                    return None
                tmp = tmp.chars[char]
            return tmp

    def reconstruct(self, i, dp, beginWord, wordList):
        if i == 0:
            return [[beginWord]]

        res = list()
        for idx in dp[i]:
            lists = self.reconstruct(idx, dp, beginWord, wordList)
            for l in lists:
                res.append(l + [wordList[i-1]])
        return res


    def findLadders(self, beginWord, endWord, wordList):
        from collections import deque
        ans = [list() for i in range(len(wordList) + 1)]
        trie, queue = Solution.TrieNode(), deque()

        for i, word in enumerate(wordList):
            trie.insertWord(i + 1, word)
        trie.insertWord(0, beginWord, dist=0)

        queue.append((0, 0, beginWord))

        while len(queue) > 0:

            idx, dist, word = queue.popleft()

            tmp = trie

            for i in range(len(word)):
                for c in tmp.chars:

                    new_word = word[:i] + c + word[i + 1:]
                    node = trie.findWord(new_word)

                    if node:
                        if node.dist < 0:
                            node.dist = dist + 1
                            queue.append((node.idx, dist + 1, new_word))

                        if node.dist > dist:
                            ans[node.idx].append(idx)

                if word[i] in tmp.chars:
                    tmp = tmp.chars[word[i]]

        node = trie.findWord(endWord)

        return self.reconstruct(node.idx, ans, beginWord, wordList) if node else []
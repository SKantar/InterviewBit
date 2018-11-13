# Word Break
# https://www.interviewbit.com/problems/word-break/
#
# Given a string s and a dictionary of words dict, determine if s can be segmented into a
# space-separated sequence of one or more dictionary words.
#
# For example, given
#
# s = "myinterviewtrainer",
# dict = ["trainer", "my", "interview"].
# Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TrieNode(object):
    def __init__(self):
        self.chars = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def __iadd__(self, word):
        tmp = self.root

        for char in word:
            if char not in tmp.chars:
                tmp.chars[char] = TrieNode()
            tmp = tmp.chars[char]

        tmp.is_word = True
        return self

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        n = len(A)
        trie, dp = Trie(), [1] + [0] * n
        for word in B:
            trie += word

        for i in range(n):
            if not dp[i]:
                continue

            curr, j = trie.root, i

            while j < n and A[j] in curr.chars:
                dp[j + 1] = max(dp[j + 1], int(curr.chars[A[j]].is_word))
                curr, j = curr.chars[A[j]], j + 1
        return dp[-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
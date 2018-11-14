# Word Break II
# https://www.interviewbit.com/problems/word-break-ii/
#
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where
# each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
#
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is
#
# [
#   "cat sand dog",
#   "cats and dog"
# ]
#
# Make sure the strings are sorted in your result.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class TrieNode:
        def __init__(self):
            self.chars = dict()
            self.marker = False

        def markWord(self):
            self.marker = True

        def insertWord(self, word):
            current = self
            for char in word:
                if char not in current.chars:
                    current.chars[char] = Solution.TrieNode()
                current = current.chars[char]
            current.markWord()

    def reconstruct(self, index, dp, sol):
        if index == 0:
            return [sol[1:]]
        result = list()
        for idx in dp[index]:
            result.extend(
                self.reconstruct(idx, dp, '{} {}'.format(
                    sol[:idx],
                    sol[idx:]
                )))
        return result

    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):

        trie = Solution.TrieNode()
        for word in B:
            trie.insertWord(word)


        dp = [list() for i in range(len(A) + 1)]
        dp[0].append(-1)

        for i in range(len(A)):
            if dp[i]:
                current, j = trie, i
                while j < len(A) and A[j] in current.chars:
                    if current.chars[A[j]].marker:
                        dp[j + 1].append(i)
                    current = current.chars[A[j]]
                    j += 1

        return sorted(self.reconstruct(-1, dp, A))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

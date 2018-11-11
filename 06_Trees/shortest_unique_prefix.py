# Shortest Unique Prefix
# https://www.interviewbit.com/problems/shortest-unique-prefix/
#
# Find shortest unique prefix to represent each word in the list.
#
# Example:
#
# Input: [zebra, dog, duck, dove]
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov
#  NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TrieNode:
    def __init__(self):
        self.chars = {}
        self.count = 0

    def __getitem__(self, index):
        return self.chars[index]

    def __setitem__(self, index, item):
        self.chars[index] = item

    def __contains__(self, item):
        return item in self.chars


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __iadd__(self, word):
        tmp = self.root

        for char in word:
            if char not in tmp:
                tmp[char] = TrieNode()
            tmp = tmp[char]
            tmp.count += 1

        return self

    def uniquePrefix(self, word):
        tmp, i = self.root, 0
        for char in word:
            tmp = tmp[char]
            i += 1
            if tmp.count == 1:
                break
        return word[:i]


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = Trie()
        for word in A:
            trie += word

        return [trie.uniquePrefix(word) for word in A]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
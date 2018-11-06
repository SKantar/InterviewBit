# Hotel Reviews
# https://www.interviewbit.com/problems/hotel-reviews/
#
# Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”, you need to sort the
# reviews in descending order according to their “Goodness Value” (Higher goodness value first). We define the “Goodness Value”
# of a string as the number of “Good Words” in that string.
#
# Note: Sorting should be stable. If review i and review j have the same “Goodness Value” then their original order would be preserved.
#
#  You are expected to use Trie in an Interview for such problems
#
# Constraints:
#
# 1.   1 <= No.of reviews <= 200
# 2.   1 <= No. of words in a review <= 1000
# 3.   1 <= Length of an individual review <= 10,000
# 4.   1 <= Number of Good Words <= 10,000
# 5.   1 <= Length of an individual Good Word <= 4
# 6.   All the alphabets are lower case (a - z)
# Input:
#
# S : A string S containing "Good Words" separated by  "_" character. (See example below)
# R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.
# Output:
#
# A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews.
#
# V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
# In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. (Indexing is 0 based)
# Example:
#
# Input:
# S = "cool_ice_wifi"
# R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
#
# Output:
# ans = [2, 0, 1]
# Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TrieNode:
    def __init__(self):
        self.chars = dict()
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __add__(self, word):
        tmp = self.root
        for char in word:
            if not char in tmp.chars:
                tmp.chars[char] = TrieNode()
            tmp = tmp.chars[char]
        tmp.word = True
        return self

    def __contains__(self, word):
        tmp = self.root
        for char in word:
            if not char in tmp.chars:
                return False
            tmp = tmp.chars[char]
        return tmp.word


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        from functools import reduce
        from collections import defaultdict
        result, trie = defaultdict(lambda: []), Trie()

        for word in A.split("_"):
            trie += word

        for i, text in enumerate(B):
            goodness_value = 0
            for word in text.split("_"):
                goodness_value += word in trie
            result[goodness_value].append(i)

        return reduce(lambda x, y: x + y, [result[key] for key in sorted(result.keys(), reverse=True)])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(Solution().solve("cool_ice_wifi", ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]))




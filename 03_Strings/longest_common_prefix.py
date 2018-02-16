# Longest Common Prefix
# https://www.interviewbit.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#
# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
#
# Example:
#
# Given the array as:
#
# [
#
#   "abcdefgh",
#
#   "aefghijk",
#
#   "abcefgh"
# ]
#
# The answer would be “a”.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = '' if not A else A[0]

        for word in A:
            i = 0
            while i < len(word) and i < len(prefix) and word[i] == prefix[i]:
                i = i + 1

            prefix = prefix[:i]

        return prefix

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(['ana', 'anastasija', 'ananas', 'anarhija', 'an']))





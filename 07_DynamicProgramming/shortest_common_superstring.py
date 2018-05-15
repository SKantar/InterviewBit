# Shortest common superstring
# https://www.interviewbit.com/problems/shortest-common-superstring/
#
# Given a set of strings. Find the length of smallest string which
# has all the strings in the set as substring
#
# Constraints:
# 1) 1 <= Number of strings <= 18
# 2) Length of any string in the set will not exceed 100.
#
# Example:
# Input: [“abcd”, “cdef”, “fgh”, “de”]
# Output: 8 (Shortest string: “abcdefgh”)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def substring(self, a, b):
        if a.find(b) != -1:
            return b
        elif b.find(a) != -1:
            return a
        return None

    def overlap(self, a, b):
        l1 = self.overlap_length(a, b)
        l2 = self.overlap_length(b, a)
        if l1 > l2:
            return l1, a, b
        else:
            return l2, b, a

    def overlap_length(self, a, b):
        length = 0
        for i in range(len(a)):
            x = len(a) - i
            if a[x:] == b[:i]:
                length = i
        return length

    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        a = [i for i in A]

        while len(a) > 1:
            item_to_remove = None
            max_overlap = None
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    item_to_remove = self.substring(a[i], a[j])
                    if item_to_remove is not None:
                        break

                    length, first, second = self.overlap(a[i], a[j])
                    if not max_overlap or max_overlap[0] < length:
                        max_overlap = length, first, second

                if item_to_remove is not None:
                    a.remove(item_to_remove)
                    break

            # print max_overlap
            if max_overlap is not None:
                length, first, second = max_overlap
                a.remove(first)
                a.remove(second)
                a.append(first + second[length:])

        return len(a[0])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

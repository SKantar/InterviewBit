# Palindrome Partitioning
# https://www.interviewbit.com/problems/palindrome-partitioning/
#
# Given a string s, partition s such that every string of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _is_palindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[-1 - i]:
                return False
        return True

    def _partition(self, A):
        if not A:
            return [[]]
        ans = []
        for i in range(len(A)):
            if self._is_palindrome(A[:i + 1]):
                for sol in self._partition(A[i + 1:]):
                    ans.append([A[:i + 1]] + sol)
        return ans

    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        return self._partition(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.partition('aab'))

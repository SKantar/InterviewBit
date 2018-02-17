# Compare Version Numbers
# https://www.interviewbit.com/problems/compare-version-numbers/
#
# Compare two version numbers version1 and version2.
#
#         If version1 > version2 return 1,
#         If version1 < version2 return -1,
#         otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _prepare(self, A):
        a = [int(tmp) for tmp in A.split('.')]
        i = len(a) - 1
        while i >= 0 and a[i] == 0:
            i -= 1
        return [0] if i == -1 else a[:i + 1]

    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a, b = self._prepare(A), self._prepare(B)
        return -1 if a < b else (1 if a > b else 0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion('01', '1'))
    print(s.compareVersion("1.2", "1.10"))


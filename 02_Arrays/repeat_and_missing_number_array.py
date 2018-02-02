# Repeat and Missing Number Array
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
#
# You are given a read only array of n integers from 1 to n.
#
# Each integer appears exactly once except A which appears twice and B which is missing.
#
# Return A and B.
#
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without
# using extra memory?
# Note that in your output A should precede B.
#
# Example:
#
# Input:[3 1 2 5 3]
# Output:[3, 4]
#
# A = 3, B = 4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        pow = lambda i: i * i

        # Sa = A1 + A2 + ... + An, Sn = 1 + 2 + ... + n
        Sa, Sn = sum(A), sum(range(1, len(A) + 1))

        # sqSa = A1^2 + A2^2 + ... + An^2, sqSn = 1^2 + 2^2 + ... + n^2
        sqSa, sqSn = sum(map(pow, A)), sum(map(pow, range(1, len(A) + 1)))

        c = Sn - Sa

        a = int(((sqSn - sqSa) / c - c) / 2)
        b = int(c + a)

        return a, b

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [3, 1, 2, 5, 3]

    s = Solution()
    print(s.repeatedNumber(A))



# Atoi
# https://www.interviewbit.com/problems/atoi/
#
# Please Note:
#
# There are certain questions where the interviewer would intentionally frame the question vague.
# The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.
#
# Implement atoi to convert a string to an integer.
#
# Example :
#
# Input : "9 2704"
# Output : 9
#
# Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
#
#     Questions:
#
#     Q1. Does string contain whitespace characters before the number?
#     A. Yes
#
#     Q2. Can the string have garbage characters after the number?
#     A. Yes. Ignore it.
#
#     Q3. If no numeric character is found before encountering garbage characters, what should I do?
#     A. Return 0.
#
#     Q4. What if the integer overflows?
#     A. Return INT_MAX if the number is positive, INT_MIN otherwise.
#
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _bound_result(self, res):
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
        elif res < -(1 << 31):
            return -(1 << 31)
        else:
            return res

    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()

        if not len(A):
            return 0

        sign = -1 if A[0] == '-' else 1
        num = A[1:] if A[0] in ['+', '-'] else A
        ans = 0

        for a in num:
            if not a.isdigit():
                return self._bound_result(sign * ans) if ans else 0
            ans = ans * 10 + ord(a) - ord('0')

        return self._bound_result(sign * ans)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.atoi("-2147483649"))




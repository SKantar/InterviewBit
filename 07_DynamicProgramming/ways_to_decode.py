# Ways to Decode
# https://www.interviewbit.com/problems/ways-to-decode/
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# Example :
#
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A or A[0] == '0':
            return 0

        prev = prev_prev = 1

        if len(A) > 1:
            prev = (1 if 10 <= int(A[:2]) <= 26 else 0) + (A[1] != '0')

        for i in range(2, len(A)):
            if A[i] == '0' and A[i - 1] not in ('1', '2'):
                return 0

            curr = prev * int(A[i] != '0') + (prev_prev if 10 <= int(A[i - 1:i + 1]) <= 26 else 0)
            prev_prev, prev = prev, curr

        return prev

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    # print(s.numDecodings("0"))
    # print(s.numDecodings("12"))
    # print(s.numDecodings("10"))
    # print(s.numDecodings("01"))
    # print(s.numDecodings("100"))
    # print(s.numDecodings("101"))
    print(s.numDecodings("110"))


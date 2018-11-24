# Stringoholics
# https://www.interviewbit.com/problems/stringoholics/
#
# You are given an array A consisting of strings made up of the letters ‘a’ and ‘b’ only.
# Each string goes through a number of operations, where:
#
#     At time 1, you circularly rotate each string by 1 letter.
#     At time 2, you circularly rotate the new rotated strings by 2 letters.
#     At time 3, you circularly rotate the new rotated strings by 3 letters.
#     At time i, you circularly rotate the new rotated strings by i % length(string) letters.
#
# Eg: String is abaa
#
#     At time 1, string is baaa, as 1 letter is circularly rotated to the back
#     At time 2, string is aaba, as 2 letters of the string baaa is circularly rotated to the back
#     At time 3, string is aaab, as 3 letters of the string aaba is circularly rotated to the back
#     At time 4, string is again aaab, as 4 letters of the string aaab is circularly rotated to the back
#     At time 5, string is aaba, as 1 letters of the string aaab is circularly rotated to the back
#
# After some units of time, a string becomes equal to it’s original self.
# Once a string becomes equal to itself, it’s letters start to rotate from the first letter again
# (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter
# will be rotated and the string will be it’s original self at 2t time.
# You have to find the minimum time, where maximum number of strings are equal to their original self.
# As this time can be very large, give the answer modulo 109+7.
#
# Note: Your solution will run on multiple test cases so do clear global variables after using them.
#
# Input:
#
# A: Array of strings.
# Output:
#
# Minimum time, where maximum number of strings are equal to their original self.
# Constraints:
#
# 1 <= size(A) <= 10^5
# 1 <= size of each string in A <= 10^5
# Each string consists of only characters 'a' and 'b'
# Summation of length of all strings <= 10^7
# Example:
#
# Input
#
# A: [a,ababa,aba]
# Output
#
# 4
#
# String 'a' is it's original self at time 1, 2, 3 and 4.
# String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
# String 'aba' is it's original self at time 2 and 4. (aba => baa => aba)
#
# Hence, 3 strings are their original self at time 4.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def gcd(self, A, B):
        if (B > A):
            A, B = B, A
        if (B == 0):
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        ans = 1
        for k in A:
            for i in range(1, 1000000000):
                if (((i * (i + 1)) // 2) % len(k) == 0):
                    ans = ((ans * i) // self.gcd(ans, i))
                    break
        return (ans % 1000000007)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
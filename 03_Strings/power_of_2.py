# Power of 2
# https://www.interviewbit.com/problems/power-of-2/
#
# Find if Given number is power of 2 or not.
# More specifically, find if given number can be expressed as 2^k where k >= 1.
#
# Input:
#
# number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
#
# Output:
#
# return 1 if the number is a power of 2 else return 0
#
# Example:
#
# Input : 128
# Output : 1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    class BigNum(str):
        def __eq__(self, other):
            if len(self) != len(other):
                return False

            for a, b in zip(self, other):
                if a != b:
                    return False

            return False

        def __mod__(self, other):
            if len(self) < 1:
                return -1
            return int(self[-1]) % 2

        def __floordiv__(self, other):
            ans = ''
            tmp = 0

            for chr in self:
                tmp = tmp * 10 + ord(chr) - ord('0')
                ans += str(tmp // 2)
                tmp = tmp % 2

            return Solution.BigNum(ans.lstrip('0'))

    # @param A : string
    # @return an integer
    def power(self, A):
        num = Solution.BigNum(A)
        while num % 2 == 0:
            if num == Solution.BigNum('2'):
                return 1
            num //= 2
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.power("0"))
    print(s.power("1"))
    print(s.power("2"))
    print(s.power("64"))
    print(s.power("4096"))

# Multiply Strings
# https://www.interviewbit.com/problems/multiply-strings/
#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
#     Note: The numbers can be arbitrarily large and are non-negative.
#     Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
#
# For example,
# given strings "12", "10", your answer should be “120”.
#
# NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
# We will retroactively disqualify such submissions and the submissions will incur penalties.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class BigNum(str):

        def _mul_num(self, a):
            ia = len(self) - 1
            no, ext = '', 0

            while ia >= 0:
                pa = (ord(self[ia]) - ord('0')) * a + ext
                no = '{}{}'.format(pa % 10, no)
                ext = pa // 10
                ia -= 1
            return Solution.BigNum('{}{}'.format(ext, no) if ext else no)

        def _shift_num(self, i):
            return Solution.BigNum('{}{}'.format(self, '0' * i))

        def __add__(self, other):
            no, ext = '', 0
            ia, ib = len(self) - 1, len(other) - 1


            while ia >= 0 or ib >= 0:
                pa = 0 if ia < 0 else ord(self[ia]) - ord('0')
                pb = 0 if ib < 0 else ord(other[ib]) - ord('0')

                no = '{}{}'.format((pa + pb + ext) % 10, no)
                ext = (pa + pb + ext) // 10

                ia, ib = ia - 1, ib - 1

            return Solution.BigNum('{}{}'.format(ext, no) if ext else no)

        def __mul__(self, other):
            ib = n = len(other) - 1
            ans = Solution.BigNum('0')

            while ib >= 0:
                no = self._mul_num(ord(other[ib]) - ord('0'))
                no = no._shift_num(n - ib)
                ans += no
                ib -= 1
            return ans

    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        ans = Solution.BigNum(A) * Solution.BigNum(B)
        ans = ans.lstrip('0')
        return '0' if not ans else ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.multiply("123123123123123", "123123123123123"))
# Valid Number
# https://www.interviewbit.com/problems/valid-number/
#
# Please Note:
#
# Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.
#
# Please think of all the corner cases and clarifications yourself.
#
# Validate if a given string is numeric.
#
# Examples:
#
#     "0" => true
#     " 0.1 " => true
#     "abc" => false
#     "1 a" => false
#     "2e10" => true
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Clarify the question using “See Expected Output”
#
#         Is 1u ( which may be a representation for unsigned integers valid?
#         For this problem, no.
#
#         Is 0.1e10 valid?
#         Yes
#
#         -01.1e-10?
#         Yes
#
#         Hexadecimal numbers like 0xFF?
#         Not for the purpose of this problem
#
#         3. (. not followed by a digit)?
#         No
#
#         Can exponent have decimal numbers? 3e0.1?
#         Not for this problem.
#
#         Is 1f ( floating point number with f as prefix ) valid?
#         Not for this problem.
#
#         How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
#         Not for this problem.
#
#         How about integers preceded by 00 or 0? like 008?
#         Yes for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        import re
        A = A.strip()

        if len(A) == 0 or (len(A) == 1 and not A.isdigit()) or not re.search('[0-9]', A):
            return 0

        no0 = re.search('^[+-]?[0-9]*(\.[0-9]+)?$', A)
        no1 = re.search('^([+-]?[0-9]*(\.[0-9]+)?)[eE][+-]?[0-9]+$', A)

        return int(bool(no0) or (bool(no1) and len(no1.group(1)) > 0 and no1.group(1) not in ['.', '+', '-']))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber(" 12341 "))
    print(s.isNumber("0"))
    print(s.isNumber(".123"))
    print(s.isNumber("01"))
    print(s.isNumber("2e0"))
    print(s.isNumber("-."))
    print(s.isNumber("46.e3"))
    print(s.isNumber(".2e3"))
    print(s.isNumber("e3"))
    print(s.isNumber(".e1"))
    print(s.isNumber("+E3"))

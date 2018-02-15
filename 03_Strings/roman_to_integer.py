# Roman To Integer
# https://www.interviewbit.com/problems/roman-to-integer/
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Read more details about roman numerals at Roman Numeric System
#
# Example :
#
# Input : "XIV"
# Return : 14
#
# Input : "XX"
# Output : 20
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def romanToInt(self, A):
        mapper = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        ans = 0

        for ara, rom in mapper:
            while A.startswith(rom):
                ans += ara
                A = A[len(rom):]
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MMMCMXCIX"))
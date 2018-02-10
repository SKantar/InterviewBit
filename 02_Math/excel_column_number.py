# Excel Column Number
# https://www.interviewbit.com/problems/excel-column-number/
#
# Given a column title as appears in an Excel sheet, return its corresponding
# column number.
#
# Example:
#
# A -> 1
#
# B -> 2
#
# C -> 3
#
# ...
#
# Z -> 26
#
# AA -> 27
#
# AB -> 28
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res = 0
        for char in A:
            diff = ord(char) - ord('A') + 1
            res = res * 26 + diff

        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber('AA'))
    print(s.titleToNumber('A'))

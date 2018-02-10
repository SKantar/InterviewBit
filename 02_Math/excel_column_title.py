# Excel Column Title
# https://www.interviewbit.com/problems/excel-column-title/
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ''

        while A:
            ans = '{}{}'.format(chr(ord('A') + (A - 1) % 26), ans)
            A = (A - 1) // 26

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(2))
    print(s.convertToTitle(3))
    print(s.convertToTitle(26))
    print(s.convertToTitle(27))
    print(s.convertToTitle(28))





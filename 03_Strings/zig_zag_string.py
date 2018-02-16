# Zigzag String
# https://www.interviewbit.com/problems/zigzag-string/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
#
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
#
# **Example 2 : **
# ABCD, 2 can be written as
#
# A....C
# ...B....D
#
# and hence the answer would be ACBD.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        res = [''] * B

        if B == 1:
            return A

        direction, i = True, 0

        for a in A:
            res[i] += a

            if direction and i == B - 1:
                direction = False
            elif not direction and i == 0:
                direction = True

            i = i + (1 if direction else -1)

        return ''.join(res)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("ABC", 2))
    print(s.convert("ABC", 1))

# Ways to color a 3xN Board
# https://www.interviewbit.com/problems/ways-to-color-a-3xn-board/
#
# Given a 3Xn board, find the number of ways to color it using at most 4 colors such that no two adjacent boxes have same color. Diagonal neighbors are not treated as adjacent boxes.
# Output the ways%1000000007 as the answer grows quickly.
#
# 1<= n < 100000
#
# Example:
# Input: n = 1
# Output: 36
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        color2, color3 = 12, 24

        for i in range(2, A + 1):
            temp = color3
            color3 = (11 * color3 + 10 * color2) % 1000000007
            color2 = (5 * temp + 7 * color2) % 1000000007
        return (color2 + color3) % 1000000007

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve(1))
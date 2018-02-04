# Pascal Triangle
# https://www.interviewbit.com/problems/pascal-triangle/
#
# Given numRows, generate the first numRows of Pascal’s triangle.
#
# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
# Example:
#
# Given numRows = 5,
#
# Return
# [
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1]
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        pascal = [[1]] if A > 0 else []

        for i in range(A - 1):
            tmp = [1]
            for j in range(1, len(pascal[i])):
                tmp.append(pascal[i][j] + pascal[i][j - 1])
            tmp.append(1)
            pascal.append(tmp)
        return pascal

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.generate(0))
    print(s.generate(1))
    print(s.generate(2))
    print(s.generate(3))
    print(s.generate(4))

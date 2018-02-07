# Kth Row of Pascal's Triangle
# https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
#
# Given an index k, return the kth row of the Pascal’s triangle.
#
# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
# Example:
#
# Input : k = 3
# Return : [1, 3, 3, 1]
#
# ''NOTE : k is 0 based. k = 0, corresponds to the row [1].''
#
# Note:Could you optimize your algorithm to use only O(k) extra space?
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    """
                1 * n * (n - 1) * (n - 2) * ... * (n - i)
        RowK(i) = ----------------------------------------------
                    1 *    2    *   3     * ... * (i + 1)


                                (n - i)
        RowK(i) = RowK(i - 1) * -------
                                (i + 1)

    """


    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row = [1]

        for i in range(A):
            row.append(row[i] * (A - i) // (i + 1))

        return row

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(0))
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))
    print(s.getRow(4))

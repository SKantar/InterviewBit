# Array 3 Pointers
# https://www.interviewbit.com/problems/array-3-pointers/
#
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
#
# **abs(x) is absolute value of x and is implemented in the following manner : **
#
#       if (x < 0) return -x;
#       else return x;
#
# Example :
#
# Input :
#         A : [1, 4, 10]
#         B : [2, 15, 20]
#         C : [10, 12]
#
# Output : 5
#          With 10 from A, 15 from B and 10 from C.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        na, nb, nc = len(A), len(B), len(C)
        ia = ib = ic = 0
        res = float('inf')

        while ia < na or ib < nb or ic < nc:
            a = A[-1] if ia == na else A[ia]
            b = B[-1] if ib == nb else B[ib]
            c = C[-1] if ic == nc else C[ic]

            res = min(max(abs(a - b), abs(b - c), abs(c - a)), res)

            if ia < na and (a <= b or ib == nb) and (a <= c or ic == nc):
                ia += 1
            elif ib < nb and (b <= a or ia == na) and (b <= c or ic == nc):
                ib += 1
            else:
                ic += 1

        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [1]
    B = [1]
    C = [1]
    print(s.minimize(A, B, C))



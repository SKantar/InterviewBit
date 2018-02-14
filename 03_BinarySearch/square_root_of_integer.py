# Square Root of Integer
# https://www.interviewbit.com/problems/square-root-of-integer/
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# If x is not a perfect square, return floor(sqrt(x))
#
# Example :
#
# Input : 11
# Output : 3
#
# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low, high = 0, A

        while low <= high:
            mid = low + (high - low) // 2

            sq_mid = mid ** 2

            if sq_mid == A:
                return mid
            elif sq_mid < A:
                if (mid + 1) ** 2 > A:
                    return mid
                low = mid + 1
            else:
                high = mid - 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.sqrt(0))


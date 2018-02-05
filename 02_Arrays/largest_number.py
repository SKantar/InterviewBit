# Largest Number
# https://www.interviewbit.com/problems/largest-number/
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example:
#
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        class Key(str):
            def __lt__(self, b):
                return self + b < b + self

        A = sorted(A, key=Key)
        return int(''.join(map(str, reversed(A))))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
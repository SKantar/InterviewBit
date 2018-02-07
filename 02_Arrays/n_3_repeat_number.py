# N/3 Repeat Number
# https://www.interviewbit.com/problems/n3-repeat-number/
#
# You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear
# time and constant additional space.
#
# If so, return the integer. If not, return -1.
#
# If there are multiple solutions, return any one.
#
# Example :
#
# Input : [1 2 3 1 1]
# Output : 1
# 1 occurs 3 times which is more than 5/3 times.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        def _calc(x, A):
            return x if len(list(filter(lambda a: a == x, A))) > len(A) / 3 else -1

        a = b = float('inf')
        cnt_a = cnt_b = 0

        for elem in A:
            if cnt_a and a == elem:
                cnt_a += 1
            elif cnt_b and b == elem:
                cnt_b += 1
            elif cnt_a == 0:
                a, cnt_a = elem, 1
            elif cnt_b == 0:
                b, cnt_b = elem, 1
            else:
                cnt_a, cnt_b = cnt_a - 1, cnt_b - 1

        x = _calc(a, A)
        if x == -1:
            return _calc(b, A)
        else:
            return x

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNumber([1, 1, 0, 3, 0, 2]))
# Largest Rectangle in Histogram
# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
#
# Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# Largest Rectangle in Histogram: Example 1
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# Largest Rectangle in Histogram: Example 2
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def largestRectangleArea(self, A):
        stack, ans = list(), 0

        for i in range(len(A)):
            if not len(stack) or A[stack[-1]] <= A[i]:
                stack.append(i)
            else:
                while len(stack) and A[stack[-1]] >= A[i]:
                    idx = stack.pop()
                    area = (i - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
                    ans = max(ans, area)
                stack.append(i)

        while len(stack):
            idx = stack.pop()
            area = (len(A) - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
            ans = max(ans, area)

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 2]))
    print(s.largestRectangleArea([4, 2, 0, 3, 2, 5]))





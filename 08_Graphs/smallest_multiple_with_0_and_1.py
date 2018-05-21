# Smallest Multiple With 0 and 1
# https://www.interviewbit.com/problems/smallest-multiple-with-0-and-1/
#
# Time Limit Exceeded. I think task has a problem with limit for python solution.
# TODO: Try to improve this
#
# You are given an integer N. You have to find smallest multiple of N which consists of
# digits 0 and 1 only. Since this multiple could be large, return it in form of a string.
#
# Note:
#
#     Returned string should not contain leading zeroes.
#
# For example,
#
# For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
# For N = 2, 10 is the answer.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        from collections import deque, defaultdict

        queue, states = deque(), defaultdict(lambda: False)
        queue.append(1)

        while True:
            curr = queue.popleft()

            if not curr % A:
                return curr

            curr = curr * 10
            for num in (curr, curr + 1):
                mod = num % A
                if not states[mod]:
                    states[mod] = True
                    queue.append(num)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.multiple(2))
    print(s.multiple(17))
    print(s.multiple(55))
# Sum Of Fibonacci Numbers
# https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
#
# How many minimum numbers from fibonacci series are required such that sum of numbers should be
# equal to a given Number N?
# Note : repetition of number is allowed.
#
# Example:
#
# N = 4
# Fibonacci numbers : 1 1 2 3 5 .... so on
# here 2 + 2 = 4
# so minimum numbers will be 2
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def generate_fib(self, A):
        arr, tmp, prev = [1], 1, 1

        while tmp <= A:
            arr.append(tmp)
            tmp, prev = tmp + prev, tmp

        return arr

    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fib, sol = self.generate_fib(A), 0
        for n in reversed(fib):
            if n > A:
                continue
            elif n == A:
                return sol + 1
            else:
                sol, A = sol + 1, A - n

        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.fibsum(2))
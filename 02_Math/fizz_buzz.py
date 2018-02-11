# FizzBuzz
# https://www.interviewbit.com/problems/fizzbuzz/
#
# Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.
#
# Example
#
# N = 5
# Return: [1 2 Fizz 4 Buzz]
#
# Note: Instead of printing the answer, you have to return it as list of strings.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def fizzBuzz(self, n):
        return [
            "{}{}{}".format(
                i if i % 3 != 0 and i % 5 != 0 else '',
                'Fizz' if i % 3 == 0 else '',
                'Buzz' if i % 5 == 0 else '',
            ) for i in range(1, n + 1)
        ]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(20))
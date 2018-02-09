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
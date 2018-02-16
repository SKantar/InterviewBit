# Count And Say
# https://www.interviewbit.com/problems/count-and-say/
#
# The count-and-say sequence is the sequence of integers beginning as follows:
#
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.
#
# 21 is read off as one 2, then one 1 or 1211.
#
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#
# Example:
#
# if n = 2,
# the sequence is 11.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        ans = "1"

        while A > 1:
            prev, res, cnt = ans[0], '', 0
            for a in ans:

                if a == prev:
                    cnt += 1
                else:
                    res += "{}{}".format(cnt, prev)
                    cnt = 1

                prev = a
            ans = res + "{}{}".format(cnt, prev)
            A -= 1

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))



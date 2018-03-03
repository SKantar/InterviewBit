# Window String
# https://www.interviewbit.com/problems/window-string/
#
# Given a string S and a string T, find the minimum window in S which will contain all the
# characters in T in linear time complexity.
# Note that when the count of a character C in T is N, then the count of C in minimum window
# in S should be at least N.
#
# Example :
#
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC"
#
#  Note:
# If there is no such window in S that covers all characters in T, return the empty string ''.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        from collections import defaultdict, deque
        dp, n = defaultdict(lambda: 0), len(B)
        word, tmp = list(), deque()

        for b in B:
            dp[b] += 1

        for a in A:
            tmp.append(a)
            if a in dp:
                n = n - 1 if dp[a] > 0 else n
                dp[a] -= 1

            if n > 0:
                continue

            while tmp:
                if tmp[0] not in dp:
                    tmp.popleft()
                elif dp[tmp[0]] < 0:
                    dp[tmp[0]] += 1
                    tmp.popleft()
                else:
                    break

            if not word or len(tmp) < len(word):
                word = list(tmp)

        return ''.join(word)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
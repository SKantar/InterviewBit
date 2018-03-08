class Solution:

    def _is_palindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[-1 - i]:
                return False
        return True

    def _partition(self, A):
        if not A:
            return [[]]
        ans = []
        for i in range(len(A)):
            if self._is_palindrome(A[:i + 1]):
                for sol in self._partition(A[i + 1:]):
                    ans.append([A[:i + 1]] + sol)
        return ans


    def partition(self, A):
        return self._partition(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.partition('aab'))

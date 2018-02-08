# Find Permutation

class Solution:

    def _reverse(self, A, i, j):
        while i < j:
            A[i], A[j] = A[j], A[i]
            i, j = i + 1, j - 1

    def findPermutation(self, A):
        res = list(range(1, len(A) + 2))

        start = None

        for i, a in enumerate(A):
            if a == 'D' and start is None:
                start = i

            if a == 'I' and start is not None:
                self._reverse(res, start, i)
                start = None

        if start is not None:
            self._reverse(res, start, len(res) - 1)

        return res



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.findPermutation("IIIII"))
    print(s.findPermutation("IIDII"))
    print(s.findPermutation("IIDID"))
    print(s.findPermutation("DIDID"))
    print(s.findPermutation("DDDII"))
    print(s.findPermutation("I"))
class Solution:
    def sortColors(self, A):
        r, b = 0, len(A) - 1
        i = 0

        while i <= b:
            if A[i] == 0:
                A[r], A[i] = A[i], A[r]
                r = r + 1
                i = max(i, r)
            elif A[i] == 2:
                A[b], A[i] = A[i], A[b]
                b = b - 1
            else:
                i += 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [0, 1, 0, 2, 1, 0]
    s.sortColors(A)
    print(A)
class Solution:

    def bs_left(self, A, B):
        """ Find left most """
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                if mid == 0 or A[mid - 1] != B:
                    return mid
                high = mid - 1
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


    def bs_right(self, A, B):
        """ Find right most """
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] == B:
                if mid + 1 >= len(A) or A[mid + 1] != B:
                    return mid
                low = mid + 1
            elif B < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchRange(self, A, B):
        return [self.bs_left(A, B), self.bs_right(A, B)]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1], 1))
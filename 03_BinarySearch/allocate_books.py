# Allocate Books
# https://www.interviewbit.com/problems/allocate-books/
#
# N number of books are given.
# The ith book has Pi number of pages.
# You have to allocate books to M number of students so that maximum number of pages alloted to a
# student is minimum. A book will be allocated to exactly one student. Each student has to be allocated
# at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated
# book 1 and book 3, skipping book 2.
#
# NOTE: Return -1 if a valid assignment is not possible
#
# Input:
#
# List of Books
# M number of students
#
# Your function should return an integer corresponding to the minimum number.
#
# Example:
#
# P : [12, 34, 67, 90]
# M : 2
#
# Output : 113
#
# There are 2 number of students. Books can be distributed in following fashion :
#   1) [12] and [34, 67, 90]
#       Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
#   2) [12, 34] and [67, 90]
#       Max number of pages is allocated to student 2 with 67 + 90 = 157 pages
#   3) [12, 34, 67] and [90]
#       Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
#
# Of the 3 cases, Option 3 has the minimum pages = 113.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:


    def number_of_students(self, A, qty):
        tmp_qty, cnt = 0, 1
        for a in A:
            tmp_qty += a
            if tmp_qty > qty:
                cnt, tmp_qty = cnt + 1, a

        return cnt



    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):

        if B > len(A):
            return -1

        l, h = max(A), sum(A)

        while l < h:
            mid = (l + h) // 2
            n = self.number_of_students(A, mid)
            if n > B:
                l = mid + 1
            else:
                h = mid
        return l

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.books([12, 34, 67, 90], 2))
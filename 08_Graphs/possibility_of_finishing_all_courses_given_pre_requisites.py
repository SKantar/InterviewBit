# Possibility of finishing all courses given pre-requisites
# https://www.interviewbit.com/problems/possibility-of-finishing-all-courses-given-prerequisites/
#
# There are a total of N courses you have to take, labeled from 1 to N. Some courses may have prerequisites,
# for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all
# courses. return 1/0 if it is possible/not possible.
# The list of prerequisite pair are given in two integer arrays B and C where B[i] is a prerequisite for C[i].
#
# Example: If N = 3 and the prerequisite pairs are [1,2] and [2,3], then you can finish courses in the following
# order: 1, 2 and 3. But if N = 2 and the prerequisite pairs are [1,2] and [2,1], then it is not possible for
# you to finish all the courses.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        from collections import deque

        paths, indegree = [list() for _ in range(A)], [0] * A

        ans = 0

        for i, j in zip(B, C):
            paths[j - 1].append(i - 1)
            indegree[i - 1] += 1

        queue = deque()

        for i in range(A):
            if not indegree[i]:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            ans += 1
            for j in paths[curr]:
                indegree[j] -= 1
                if not indegree[j]:
                    queue.append(j)

        return int(ans == A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve(3, [1, 2], [2, 3]))
    print(s.solve(2, [1, 2], [2, 1]))


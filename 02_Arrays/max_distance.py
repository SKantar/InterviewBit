# Max Distance
# https://www.interviewbit.com/problems/max-distance/
#
# If there is no solution possible, return -1.
#
# Example:
#
# A : [3 5 4 2]
#
# Output : 2
# for the pair (3, 4)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        dp_min, minn = list(), float('inf')
        dp_max, maxx = list(), -float('inf')

        for tmp_min, tmp_max in zip(A, reversed(A)):
            minn = min(minn, tmp_min)
            dp_min.append(minn)

            maxx = max(tmp_max, maxx)
            dp_max.append(maxx)

        dp_max.reverse()

        i = j = ans = 0
        while i < len(A) and j < len(A):
            if dp_min[i] <= dp_max[j]:
                ans = max(j - i, ans)
                j += 1
            else:
                i += 1

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.maximumGap([3, 5, 4, 2]))
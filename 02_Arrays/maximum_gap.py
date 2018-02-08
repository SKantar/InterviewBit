# Maximum Consecutive Gap
# https://www.interviewbit.com/problems/maximum-consecutive-gap/
#
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Example :

# Input : [1, 10, 5]
# Output : 5
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume that all the elements in the array are non-negative
# integers and fit in the 32-bit signed integer range.
#
# You may also assume that the difference will not overflow.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class Bucket:
        def __init__(self):
            self.low = float('inf')
            self.high = -float('inf')

        def __repr__(self):
            return "<{} {}>".format(self.low, self.high)

    def _min_max(self, A):
        maxx, minn = -float('inf'), float('inf')

        for a in A:
            maxx = max(a, maxx)
            minn = min(a, minn)

        return minn, maxx

    def maximumGap(self, A):

        if len(A) < 2:
            return 0

        buckets = [Solution.Bucket() for i in range(len(A) + 1)]
        minn, maxx = self._min_max(A)

        if minn == maxx:
            return 0

        interval = len(A) / (maxx - minn)

        for a in A:
            i = int(interval * (a - minn))

            buckets[i].low = min(buckets[i].low, a)
            buckets[i].high = max(buckets[i].high, a)

        prev, ans = buckets[0].high, 0
        for i in range(1, len(buckets)):
            if buckets[i].low < float('inf'):
                ans = max(ans, buckets[i].low - prev)
                prev = buckets[i].high

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.maximumGap([1, 10, 5]))


# Merge Overlapping Intervals
# https://www.interviewbit.com/problems/merge-overlapping-intervals/
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example:
#
# Given [1,3],[2,6],[8,10],[15,18],
#
# return [1,6],[8,10],[15,18].
#
# Make sure the returned intervals are sorted.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for an interval.
# class Interval:
#     def __init__(self, s, e):
#         self.start = s
#         self.end = e
#
#     def __repr__(self):
#         return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):

        class Key(Interval):
            def __init__(self, interval):
                super().__init__(interval.start, interval.end)

            def __lt__(self, other):
                if self.start == other.start:
                    return self.end < other.end
                return self.start < other.start

        if not intervals:
            return []

        intervals, ans = sorted(intervals, key=Key), list()

        start, end = intervals[0].start, intervals[0].end

        for i in range(len(intervals)):
            end = max(end, intervals[i].end)

            if i == len(intervals) - 1 or intervals[i + 1].start > end:
                ans.append(Interval(start, end))
                if i != len(intervals) - 1:
                    start = intervals[i + 1].start
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    lst = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    s = Solution()
    print(s.merge(lst))

    lst = []
    s = Solution()
    print(s.merge(lst))

    lst = [Interval(1, 4), Interval(2, 3)]
    s = Solution()
    print(s.merge(lst))
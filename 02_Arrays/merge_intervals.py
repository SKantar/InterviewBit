# Merge Intervals
# https://www.interviewbit.com/problems/merge-intervals/
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
#
# Example 2:
#
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#
# Make sure the returned intervals are also sorted.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
#     def __repr__(self):
#         return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        i = 0
        while i < len(intervals) and intervals[i].start < new_interval.start:
            i += 1

        intervals.insert(i, new_interval)

        return self.merge(intervals)

    def merge(self, intervals):
        ans = list()
        start, end = intervals[0].start, intervals[0].end

        for i in range(len(intervals)):
            end = max(end, intervals[i].end)

            if i == len(intervals) - 1 or intervals[i + 1].start > end:
                ans.append(Interval(start, end))
                if i < len(intervals) - 1:
                    start = intervals[i + 1].start
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 9)))








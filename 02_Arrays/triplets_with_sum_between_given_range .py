# Triplets with Sum between given range
# https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/
#
# Given an array of real numbers greater than zero in form of strings.
# Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
# Return 1 for true or 0 for false.
#
# Example:
#
# Given [0.6, 0.7, 0.8, 1.2, 0.4] ,
#
# You should return 1
#
# as
#
# 0.6+0.7+0.4=1.7
#
# 1<1.7<2
#
# Hence, the output is 1.
#
# O(n) solution is expected.
#
# Note: You can assume the numbers in strings don’t overflow the primitive data type and there are
# no leading zeroes in numbers. Extra memory usage is allowed.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    """ define 3 intervals
    |            X           |               |              |
    |        [0, 2/3)        |       Y       |       Z      |
    |                        |   [2/3, 1]    |    (1, 2)    |
    |       X1        X2     |               |              |
    |    [0, 1/2) [1/2, 2/3) |               |              |

    CASE A: X X X   min1X, min2X, min3X
    CASE B: X X Y
        CASE B1: X1 X2 Y    min1X1 min1X2 minY
        CASE B2: X1 X1 Y    max1X1 max2X1 maxY
        CASE B3: X2 X2 Y    min1X1 min2X1 minY

    CASE C: X X Z   min1X, min1Y, min1Z
    CASE D: X Y Y   min1X, min1Y, min2Y
    CASE E: X Y Z   min1X, min1Y, min1Z


    """
    def _inX(self, x):
        """ in X interval """
        return 0 <= x < 2 / 3

    def _inY(self, x):
        """ in Y interval """
        return 2 / 3 <= x <= 1

    def _inX1(self, x):
        """ in X1 interval """
        return 0 <= x < 1/2

    def _inX2(self, x):
        """ in X2 interval """
        return 1/2 <= x < 2/3

    def max3(self, max1, max2, max3, current):
        """ Update max of 3 elements """
        if current >= max1:
            return current, max1, max2
        elif current >= max2:
            return max1, current, max2
        elif current > max3:
            return max1, max2, current
        return max1, max2, max3

    def max2(self, max1, max2, current):
        """ Update max of 2 elements """
        if current >= max1:
            return current, max1
        elif current >= max2:
            return max1, current
        return max1, max2

    def min2(self, min1, min2, current):
        """ Update min of 2 elements """
        if current <= min1:
            return current, min1
        elif current <= min2:
            return min1, current
        return min1, min2

    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        A = map(float, A)
        min1X = min2X = float('inf')
        max1X = max2X = max3X = -float('inf')
        min1Z = min1Y = min2Y = float('inf')
        max1Y = max1X1 = max2X1 = -float('inf')
        min1X2 = min2X2 = min1X1 = float('inf')

        for a in A:
            if self._inX(a):
                max1X, max2X, max3X = self.max3(max1X, max2X, max3X, a)
                min1X, min2X = self.min2(min1X, min2X, a)
                if self._inX1(a):
                    max1X1, max2X1 = self.max2(max1X1, max2X1, a)
                    min1X1 = min(min1X1, a)
                elif self._inX2(a):
                    min1X2, min2X2 = self.min2(min1X2, min2X2, a)
            elif self._inY(a):
                min1Y, min2Y = self.min2(min1Y, min2Y, a)
                max1Y = max(max1Y, a)
            else:
                min1Z = min(min1Z, a)

        if 1 < max1X + max2X + max3X < 2:       # CASE A
            return 1
        elif 1 < min1X1 + min1X2 + min1Y < 2:   # CASE B1
            return 1
        elif 1 < max1X1 + max2X1 + max1Y < 2:   # CASE B2
            return 1
        elif 1 < min1X2 + min2X2 + min1Y < 2:   # CASE B3
            return 1
        elif 1 < min1X + min2X + min1Z < 2:     # CASE C
            return 1
        elif 1 < min1X + min1Y + min2Y < 2:     # CASE D
            return 1
        elif 1 < min1X + min1Y + min1Z < 2:     # CASE E
            return 1
        else:
            return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.solve(["2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191"]))
    print(s.solve(["2.445610", "0.129967", "2.376455", "1.910948", "0.917844", "0.815911", "1.743973"]))
    print(s.solve(["0.628934", "0.939859", "0.898308", "1.251313", "1.380492", "1.070370", "0.701036", "1.349819", "1.277858", "1.171202"]))
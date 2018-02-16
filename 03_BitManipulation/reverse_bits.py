class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        head, tail = 1 << 31, 1

        for i in range(16):
            not_same = int(n & head > 0) ^ int(n & tail > 0)

            if not_same:
                n = n ^ tail ^ head

            head >>= 1
            tail <<= 1
        return n

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(43261596))
    print(s.reverseBits(32768))
    print(s.reverseBits(0))
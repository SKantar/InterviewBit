# Valid Ip Addresses
# https://www.interviewbit.com/problems/valid-ip-addresses/
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
#
# Example:
#
# Given “25525511135”,
#
# return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        ans = list()
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):
                        if i + j + k + l == len(A):
                            parts = A[:i], A[i:i+j], A[i+j:i+j+k], A[i+j+k:]
                            for part in parts:
                                if len(part) != len(str(int(part))) or int(part) > 255:
                                    break
                            else:
                                ans.append('.'.join(parts))
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("010010"))
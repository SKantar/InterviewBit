# Pretty Json
# https://www.interviewbit.com/problems/pretty-json/
#
# Pretty print a json object using proper indentation.
#
#     Every inner brace should increase one indentation to the following lines.
#     Every close brace should decrease one indentation to the same line and the following lines.
#     The indents can be increased with an additional ‘\t’
#
# Example 1:
#
# Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
# Output :
# {
#     A:"B",
#     C:
#     {
#         D:"E",
#         F:
#         {
#             G:"H",
#             I:"J"
#         }
#     }
# }
#
# Example 2:
#
# Input : ["foo", {"bar":["baz",null,1.0,2]}]
# Output :
# [
#     "foo",
#     {
#         "bar":
#         [
#             "baz",
#             null,
#             1.0,
#             2
#         ]
#     }
# ]
#
# [] and {} are only acceptable braces in this case.
#
# Assume for this problem that space characters can be done away with.
#
# Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        import re

        A, tmp, ans = re.sub(r'\s+', '', A), '', []
        ident, i, newline = 0, 0, False

        while i < len(A):

            if A[i] in ['}', '{', '[', ']'] and i > 0:
                ans.append(tmp)
                tmp, newline = '', True
                ident -= (A[i] in ['}', ']'])

            tmp = (tmp + '\t' * ident + A[i]) if newline else (tmp + A[i])
            newline = False

            ident = ident + (A[i] in ['{', '['])

            if A[i] in [',', '{', '['] and (i < len(A) - 1 and A[i + 1] not in ['{', '[']):
                ans.append(tmp)
                tmp, newline = '', True

            i += 1

        ans.append(tmp)

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'))
    print(s.prettyJSON('["foo", {"bar":["baz",null,1.0,2]}]'))

    for line in s.prettyJSON('"{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}"'):
        print(line)
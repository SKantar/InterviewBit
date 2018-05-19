# Simplify Directory Path
# https://www.interviewbit.com/problems/simplify-directory-path/
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# Examples:
#
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        entries = A.split('/')
        new_path = []
        for e in entries:
            if e == '..':
                if new_path:
                    new_path.pop()
            elif e != '.':
                new_path.append(e)
        new_path = [p for p in new_path if p]
        return '/' + '/'.join(new_path)


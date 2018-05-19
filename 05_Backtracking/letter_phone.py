# Letter Phone
# https://www.interviewbit.com/problems/letter-phone/
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# The digit 0 maps to 0 itself.
# The digit 1 maps to 1 itself.
#
# Input: Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Make sure the returned strings are lexicographically sorted.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    MAP = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }


    def _letterCombinations(self, i, A, sub):
        if(i == len(A) - 1):
            return [sub + char for char in Solution.MAP[A[i]]]

        res = list()
        for char in Solution.MAP[A[i]]:
           res.extend(self._letterCombinations(i + 1, A, sub + char))
        return res


    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        return self._letterCombinations(0, A, '')

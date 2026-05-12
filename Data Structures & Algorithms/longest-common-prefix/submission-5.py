class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" # empty string if no common prefix

        for i in range(len(strs[0])): 
            """iterate through all of the strings 
                or it is not the shortest string"""
            for s in strs: # iterate through every string and they have the same exact char at index i
                if i == len(s) or s[i] != strs[0][i]: # if in bounds or if not equal, return the result
                    return res
            res += strs[0][i]
        return res

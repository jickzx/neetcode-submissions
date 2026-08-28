class Solution:
    def validPalindrome(self, s: str) -> bool:
        # for loop, return true/false, etc
        if s != s[::-1]:
            return True
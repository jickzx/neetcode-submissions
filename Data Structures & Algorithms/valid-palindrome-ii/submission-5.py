class Solution:
    def validPalindrome(self, s: str) -> bool:
        # for loop, return true/false, etc
        if s == s[::-1]:
            return True
        
        for i in range(len(s)):
            ns = s[:i] + s[i+1:]
            if ns == ns[::-1]:
                return True
        return False
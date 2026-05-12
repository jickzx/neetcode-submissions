class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        # Solution 2
        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric characters from the right
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
            
        return True

    # Helper function to check if a character is alphanumeric
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
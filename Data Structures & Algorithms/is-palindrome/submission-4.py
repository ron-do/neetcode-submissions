class Solution:
    def checkValidAscii(self, char):
        return (
            ord('Z') >= ord(char) >= ord('A') or
            ord('9') >= ord(char) >= ord('0') or
            ord('z') >= ord(char) >= ord('a')
        )

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.checkValidAscii(s[l]):
                l += 1
            while r > l and not self.checkValidAscii(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
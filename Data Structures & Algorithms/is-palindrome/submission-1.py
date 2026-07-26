class Solution:
    def check_valid_char(self, char):
        asc = ord(char)
        if ord('A') <= asc <= ord('Z') or ord('a') <= asc <= ord('z') or ord('0') <= asc <= ord('9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1

        while head < tail:
            head_word = s[head].lower()
            tail_word = s[tail].lower()

            if not self.check_valid_char(head_word):
                head += 1
                continue
            if not self.check_valid_char(tail_word):
                tail -= 1
                continue
            
            if head_word != tail_word:
                return False
            
            head += 1
            tail -= 1

        return True
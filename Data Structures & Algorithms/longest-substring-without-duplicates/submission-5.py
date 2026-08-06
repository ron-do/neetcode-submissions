class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            char = s[r]

            while char in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(char)
            max_len = max(max_len, len(char_set))

        return max_len
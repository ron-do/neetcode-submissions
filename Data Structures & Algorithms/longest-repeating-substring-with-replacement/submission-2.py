class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = defaultdict(int)
        l = 0
        most_char = 0
        ret = 0

        for r in range(len(s)):
            char_dict[s[r]] += 1
            
            most_char = max(most_char, char_dict[s[r]])
            while (r - l + 1) - most_char > k:
                char_dict[s[l]] -= 1
                l += 1
            
            ret = max(ret, r - l + 1)

        return ret
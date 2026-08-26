class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        ret = 0

        l = 0
        _max = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            _max = max(_max, char_count[s[r]])

            while r - l + 1 - _max > k:
                char_count[s[l]] -= 1
                l += 1
            
            ret = max(ret, r - l + 1)
        return ret
            
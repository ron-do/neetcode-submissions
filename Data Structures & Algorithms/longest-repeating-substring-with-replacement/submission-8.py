class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        ret = 0
        most_freq = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(most_freq, freq[s[r]])

            while (r - l + 1) - most_freq > k:
                freq[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1)

        return ret

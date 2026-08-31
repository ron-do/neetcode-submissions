class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        window_freq = defaultdict(int)

        for char in s1:
            s1_freq[char] += 1

        l = 0
        r = len(s1)

        for char in s2[l:r]:
            window_freq[char] += 1

        print(window_freq)

        if window_freq == s1_freq:
            return True
        
        for r in range(len(s1), len(s2)):            
            window_freq[s2[r]] += 1
            window_freq[s2[l]] -= 1

            if window_freq[s2[l]] == 0:
                del window_freq[s2[l]]

            l += 1

            print(window_freq, s1_freq)

            if window_freq == s1_freq:
                return True

        return False

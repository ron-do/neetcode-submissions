class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            ret += f"{len(string)}#{string}"
        
        return ret

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        ret = []
        while r < len(s):
            if s[r] != "#":
                r += 1
                continue
            
            string_len = int(s[l:r])
            l = r + 1
            r = r + string_len + 1
            string = s[l:r]
            ret.append(string)
            l = r

        return ret
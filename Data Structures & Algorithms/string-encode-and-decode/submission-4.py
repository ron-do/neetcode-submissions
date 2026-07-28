class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = []
        for string in strs:
            ret.append(str(len(string)))
            ret.append("$")
            ret.append(string)
        
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        ret = []
        start = 0

        while start < len(s):
            end = start
            while s[end] != "$":
                end += 1

            _len = int(s[start:end])

            start = end + 1
            end = start + _len
            string = s[start:end]
            ret.append(string)
            start = end
        return ret

            
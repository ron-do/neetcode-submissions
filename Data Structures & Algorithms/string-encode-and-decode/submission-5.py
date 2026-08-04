class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            str_len = len(string)
            ret += f"{str_len}${string}"

        return ret

    def decode(self, s: str) -> List[str]:
        head = 0
        tail = 0
        ret = []
        while head < len(s):
            if s[head] != "$":
                head += 1
                continue
            
            str_len = int(s[tail:head])
            head += 1
            ret.append(s[head:head + str_len])
            head += str_len
            tail = head
        return ret 

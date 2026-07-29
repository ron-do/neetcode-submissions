class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}

        for string in strs:
            alpha = [0] * 26
            for char in string:
                alpha[ord(char) - ord('a')] += 1

            alpha = tuple(alpha)
            
            if alpha in _dict:
                _dict[alpha].append(string)
            else:
                _dict[alpha] = [string]

        ret = []

        for strings in _dict.values():
            ret.append(strings)

        return ret
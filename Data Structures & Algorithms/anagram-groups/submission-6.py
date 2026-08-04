class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}

        for string in strs:
            alphabet_count = [0] * 26

            for char in string:
                alphabet_count[ord(char) - ord('a')] += 1
            
            alphabet_count = tuple(alphabet_count)
            if alphabet_count in _dict:
                _dict[alphabet_count].append(string)
            else:
                _dict[alphabet_count] = [string]
        
        ret = []

        for strings in _dict.values():
            ret.append(strings)

        return ret
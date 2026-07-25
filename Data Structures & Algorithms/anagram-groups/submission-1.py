class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}

        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string in _dict:
                _dict[sorted_string].append(string) 
            else:
                _dict[sorted_string] = [string]

        ret = []

        for value in _dict.values():
            ret.append(value)

        return ret
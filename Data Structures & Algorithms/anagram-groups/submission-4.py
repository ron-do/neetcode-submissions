class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for string in strs:
            key = [0] * 26
            for char in string:
                idx = ord(char) - ord('a')
                key[idx] += 1
            
            key = tuple(key)
            if key in freq:
                freq[key].append(string)
            else:
                freq[key] = [string]
        
        ret = []
        for val in freq.values():
            ret.append(val)

        return ret
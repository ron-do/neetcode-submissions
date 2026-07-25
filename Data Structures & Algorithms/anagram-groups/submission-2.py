class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        characters = 'abcdefghijklmnopqrstuvwxyz'

        for string in strs:
            arr = [0] * 26
            for letter in string:
                arr[ord(letter) - 97] += 1
            
            _dict[tuple(arr)].append(string)
        
        ret = []
        for value in _dict.values():
            ret.append(value)

        return ret
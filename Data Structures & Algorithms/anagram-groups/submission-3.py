class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        characters = 'abcdefghijklmnopqrstuvwxyz'

        for string in strs:
            arr = [0] * 26
            for letter in string:
                arr[ord(letter) - ord('a')] += 1
            
            _dict[tuple(arr)].append(string)
        
        return list(_dict.values())
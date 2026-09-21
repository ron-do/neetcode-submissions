class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = defaultdict(int)
        ret = []

        for n in nums:
            _dict[n] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        
        for key, val in _dict.items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, -1, -1):
            while freq[i]:
                if k == 0:
                    return ret
                ret.append(freq[i].pop())
                k -= 1

        return ret
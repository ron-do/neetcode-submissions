class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = defaultdict(int)
        ret = []

        for num in nums:
            _dict[num] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in _dict.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, -1, -1):
            while freq[i] and k > 0:
                k -= 1
                ret.append(freq[i].pop())

        return ret
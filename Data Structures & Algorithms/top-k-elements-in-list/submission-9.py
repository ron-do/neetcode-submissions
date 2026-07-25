class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num in _dict:
                _dict[num] += 1
            else:
                _dict[num] = 1

        for num, count in _dict.items():
            freq[count].append(num)

        ret = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
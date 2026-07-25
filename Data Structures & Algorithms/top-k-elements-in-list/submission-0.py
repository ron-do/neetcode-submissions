class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = {}

        for num in nums:
            if num in _dict:
                _dict[num] += 1
            else:
                _dict[num] = 1

        arr = []
        for key, value in _dict.items():
            arr.append((key, value))
        arr.sort(key=lambda x: x[1], reverse=True)

        ret = []
        for i in range(k):
            ret.append(arr[i][0])
        return ret

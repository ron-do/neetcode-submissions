class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        for num, value in freq_dict.items():
            freq[value].append(num)

        ret = []
        i = len(freq) - 1
        while k > 0 and i >= 0:
            if freq[i]:
                for item in freq[i]:
                    ret.append(item)
                    k -= 1
            i -= 1

        return ret
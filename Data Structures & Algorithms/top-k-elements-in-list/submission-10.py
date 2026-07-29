class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        ret = []

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        while k > 0:
            max_key = max(freq_dict, key=freq_dict.get)
            ret.append(max_key)
            freq_dict[max_key] = 0
            k -= 1
        return ret
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        freq_list = [[] for _ in range(len(nums) + 1)]
        ret = []

        for num, freq in freq_dict.items():
            freq_list[freq].append(num)

        i = len(freq_list) - 1
        while k > 0:
            while freq_list[i]:
                k -= 1
                ret.append(freq_list[i].pop())
            i -= 1

        return ret
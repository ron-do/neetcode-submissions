class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        freq_list = [[] for _ in range(len(nums) + 1)]

        for key, val in freq_dict.items():
            print(val)
            freq_list[val].append(key)

        ret = []
        i = len(freq_list) - 1
        while k > 0:
            if freq_list[i]:
                while freq_list[i]:
                    ret.append(freq_list[i].pop())
                    k -= 1
            i -= 1
        
        return ret
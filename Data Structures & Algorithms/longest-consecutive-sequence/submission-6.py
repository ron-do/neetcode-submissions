class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 1

        for num in num_set:
            length = 1
            if num - 1 not in num_set:
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _dict = {}
        for num in nums:
            if num in _dict:
                return True
            else:
                _dict[num] = 1
        return False
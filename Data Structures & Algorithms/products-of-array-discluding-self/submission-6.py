class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        ret = [1] * len(nums)

        for i in range(len(nums)):
            ret[i] = left
            left *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= right
            right *= nums[i]
        
        return ret
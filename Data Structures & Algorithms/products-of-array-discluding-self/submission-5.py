class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ret = [1] * len(nums)

        for i in range(len(nums)):
            ret[i] = mul
            mul *= nums[i]

        mul = 1

        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= mul
            mul *= nums[i]

        return ret
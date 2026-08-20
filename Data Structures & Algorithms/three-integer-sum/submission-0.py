class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                elif r < len(nums) - 2 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif _sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return ret
                
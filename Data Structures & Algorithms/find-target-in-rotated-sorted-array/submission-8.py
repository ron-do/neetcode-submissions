class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ret = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            
            if nums[mid] == target:
                ret = mid
                break

            # 언덕이 오른쪽에 있음 - 왼쪽이 정상 정렬 상태
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return ret
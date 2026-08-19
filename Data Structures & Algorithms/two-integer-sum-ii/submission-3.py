class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        ret = []

        while left < right:            
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                ret.append(left + 1)
                ret.append(right + 1)
                break
            elif _sum > target:
                right -= 1
            else:
                left += 1

        return ret        

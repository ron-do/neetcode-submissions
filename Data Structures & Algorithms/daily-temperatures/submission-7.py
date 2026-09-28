class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][1]:
                idx, _ = temp_stack.pop()
                ret[idx] = i - idx
            temp_stack.append((i, temp))

        return ret
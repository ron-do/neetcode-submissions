class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []
        temp_list = []

        for i, t in enumerate(temperatures):
            temp_list.append((t, i))

        for t, i in temp_list:
            while temp_stack and t > temp_stack[-1][0]:
                _, ii = temp_stack.pop()
                result[ii] = i - ii

            temp_stack.append((t, i))

        return result
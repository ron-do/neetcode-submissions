class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        num_stack = []

        for t in tokens:
            if t not in operators:
                num_stack.append(int(t))
                continue

            num1 = num_stack.pop()
            num2 = num_stack.pop()

            if t == "+":
                num_stack.append(num1 + num2)
            elif t == "-":
                num_stack.append(num2 - num1)
            elif t == "*":
                num_stack.append(num1 * num2)
            elif t == "/":
                num_stack.append(int(num2 / num1))

        return num_stack[-1]
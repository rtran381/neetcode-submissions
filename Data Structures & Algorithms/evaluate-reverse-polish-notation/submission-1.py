class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case "+":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x + y)
                case "-":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x - y)
                case "*":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x * y)
                case "/":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(int(x / y))
                case _:
                    stack.append(int(t))
        return stack.pop()

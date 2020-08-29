from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        math = {
            '+': lambda a, b: int(a) + int(b),
            '-': lambda a, b: int(a) - int(b),
            '*': lambda a, b: int(a) * int(b),
            '/': lambda a, b: int(int(a) / int(b)),
        }

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                do_math = math[i](a, b)
                stack.append(do_math)

        return stack.pop()


assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6

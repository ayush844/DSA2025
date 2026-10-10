class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        valid_op = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y)
        }

        for token in tokens:
            if token in valid_op:
                n2 = stack.pop()
                n1 = stack.pop()
                new = valid_op[token](n1, n2)
                stack.append(new)
            else:
                stack.append(int(token))

        
        return stack.pop()
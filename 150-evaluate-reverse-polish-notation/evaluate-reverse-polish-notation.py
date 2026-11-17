class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        valid_operators = {
            '+': lambda n1, n2: n1+n2,
            '-': lambda n1, n2: n1-n2,
            '*': lambda n1, n2: n1*n2,
            '/': lambda n1, n2: int(n1/n2)
        }

        for token in tokens:
            if token in valid_operators:
                n2 = stack.pop()
                n1 = stack.pop()

                res = valid_operators[token](n1, n2)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
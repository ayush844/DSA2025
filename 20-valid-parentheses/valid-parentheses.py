class Solution:
    def isValid(self, s: str) -> bool:
        mapped_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for ch in s:
            if ch not in mapped_brackets:
                stack.append(ch)
            else:
                if not stack:
                    return False

                last_ch = stack.pop()
                if mapped_brackets[ch] != last_ch:
                    return False

        return len(stack) == 0
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for i in s:
            dict[i] = 1 + dict.get(i, 0)

        for i, char in enumerate(s):
            if dict[char] == 1:
                return i

        return -1
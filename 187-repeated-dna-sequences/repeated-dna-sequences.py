class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        output = set()
        L = 10
        n = len(s)

        for i in range(n-L+1):
            text = s[i: i+L]
            if text in seen:
                output.add(text)
            seen.add(text)

        return list(output)
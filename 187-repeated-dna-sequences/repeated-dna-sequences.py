class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L = 10
        n = len(s)
        seen = set()
        output = set()

        for i in range(n-L+1):
            text = s[i:i+L]
            if text in seen:
                output.add(text)
            seen.add(text)

        return list(output)
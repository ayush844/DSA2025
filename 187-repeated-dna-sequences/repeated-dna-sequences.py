class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        seen = set()
        output = set()
        for i in range(n-L+1):
            temp = s[i:i+L]
            if temp in seen:
                output.add(temp)
            seen.add(temp)

        return list(output)
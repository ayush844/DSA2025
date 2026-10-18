class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        l = 10
        n = len(s)
        output = set()
        seen = set()

        for i in range(n-l+1):
            seq = s[i: i+l]
            if seq in seen:
                output.add(seq)
            
            seen.add(seq)

        return list(output)
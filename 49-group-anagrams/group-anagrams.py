class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return []

        sorted_strs = ["".join(sorted(text)) for text in strs]

        ht = {}

        for i, text in enumerate(sorted_strs):
            if text in ht:
                ht[text].append(strs[i])
            else:
                ht[text] = [strs[i]]

        return list(ht.values())
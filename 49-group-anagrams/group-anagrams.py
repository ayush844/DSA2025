class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        sorted_strs = ["".join(sorted(text)) for text in strs]

        hash = {}

        for i, text in enumerate(sorted_strs):
            if text in hash:
                hash[text].append(strs[i])
            else:
                hash[text] = [strs[i]]

        return list(hash.values())
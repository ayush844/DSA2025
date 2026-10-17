class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)

        sorted_strs = ["".join(sorted(text)) for text in strs]

        hash_map = {}

        for i, text in enumerate(sorted_strs):
            if text in hash_map:
                hash_map[text].append(strs[i])
            else:
                hash_map[text] = [strs[i]]

        return list(hash_map.values())
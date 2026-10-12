class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = {}

        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        sorted_num = sorted(hash.keys(), key = lambda num: hash[num], reverse=True)

        return sorted_num[:k]
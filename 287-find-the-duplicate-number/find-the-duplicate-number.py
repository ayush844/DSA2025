class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hare = 0
        tortoise = 0

        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]

            if hare == tortoise:
                tortoise = 0
                while tortoise != hare:
                    tortoise = nums[tortoise]
                    hare = nums[hare]

                return tortoise
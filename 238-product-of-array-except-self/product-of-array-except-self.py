class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeroes = []
        non_zero = []
        n = len(nums)
        product = 1

        for i in range(n):
            if nums[i] == 0:
                zeroes.append(i)
            else:
                non_zero.append(i)
                product*=nums[i]

        res = []
        if len(zeroes) == 0:
            for i in range(n):
                res.append(product//nums[i])
            return res
        
        if len(zeroes) > 1:
            return [0 for _ in range(n)]

        for i in range(n):
            if i == zeroes[0]:
                res.append(product)
            else:
                res.append(0)

        return res
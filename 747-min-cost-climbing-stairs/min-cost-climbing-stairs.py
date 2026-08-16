class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        minCost = [-1]*n

        def helper(index):

            if index > n-1:
                return 0
            
            if minCost[index] != -1:
                return minCost[index]

            oneStep = cost[index] + helper(index+1)
            twoStep = cost[index] + helper(index+2)

            minCost[index] = min(oneStep, twoStep)

            return minCost[index]


        return min(helper(0), helper(1))
        
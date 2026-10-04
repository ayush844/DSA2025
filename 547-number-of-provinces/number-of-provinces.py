class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def dfs(city):
            for neighour in range(n):
                if isConnected[city][neighour] == 1 and not visited[neighour]:
                    visited[neighour] = True
                    dfs(neighour)

        count = 0
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                count+=1

        return count
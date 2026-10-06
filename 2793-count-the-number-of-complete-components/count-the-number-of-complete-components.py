class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_lst = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        def dfs(node):
            visited.add(node)
            component.append(node)
            for neighour in adj_lst[node]:
                if neighour not in visited:
                    dfs(neighour)

        count = 0
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i)

                k = len(component)

                if all(len(adj_lst[node]) == k-1 for node in component):
                    count+=1


        return count
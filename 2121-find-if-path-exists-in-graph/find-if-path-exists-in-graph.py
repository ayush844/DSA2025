class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[]*n for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([source])
        visited = set([source])

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for neighour in graph[node]:
                if neighour not in visited:
                    visited.add(neighour)
                    q.append(neighour)

        return False
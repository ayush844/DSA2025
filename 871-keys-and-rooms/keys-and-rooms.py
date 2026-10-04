class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = deque()
        visited = set([0])

        for key in rooms[0]:
            if key not in visited:
                q.append(key)
                visited.add(key)

        while q:
            i = q.popleft()
            for key in rooms[i]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)

        if len(visited) == len(rooms):
            return True

        return False
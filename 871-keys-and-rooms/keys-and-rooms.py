class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = deque()
        visited = set([0])

        for key in rooms[0]:
            q.append(key)
            visited.add(key)

        while q:
            room_num = q.popleft()
            for key in rooms[room_num]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)

        if len(visited) == len(rooms):
            return True
        
        return False
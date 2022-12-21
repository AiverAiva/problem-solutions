class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        def dfs(room):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)
        dfs(0)
        return all(visited)
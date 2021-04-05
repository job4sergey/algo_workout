class Solution(object):
    def canVisitAllRooms(self, rooms):
        vis = [False] * len(rooms)
        vis[0] = True
        cn = len(rooms) - 1

        def dfs(k0):
            nonlocal cn
            if cn == 0:
                return

            for k in rooms[k0]:
                if not vis[k]:
                    vis[k] = True
                    cn -= 1
                    dfs(k)

                if cn == 0:
                    return

        dfs(0)
        return cn == 0

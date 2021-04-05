class Solution(object):
    def canVisitAllRooms(self, rooms):
        vis = [False] * len(rooms)
        vis[0] = True
        q = []

        def enq(k0):
            for k in rooms[k0]:
                if not vis[k]:
                    vis[k] = True
                    q.append(k)

        enq(0)

        def doit():
            cn = len(rooms) - 1
            while q and cn:
                k = q.pop()
                enq(k)
                cn -= 1
            return cn == 0

        return doit()

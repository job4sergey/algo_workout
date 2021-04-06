class Solution:
    def maxAreaOfIsland(self, g):
        rc = len(g)
        if not rc: return 0
        cc = len(g[0])
        if not cc: return 0
        
        mx = 0
        def dfs(g, r0, c0, mx):
            nonlocal rc, cc
            if g[r0][c0] != 1: return mx
            
            st = [(r0, c0)]
            g[r0][c0] = -1
            
            def push(g, st, r, c):
                if r < 0 or r == rc or c < 0 or c == cc or g[r][c] != 1: return
                g[r][c] = -1
                st.append((r, c))
                
            cn = 0
            
            while st:
                r, c = st.pop()
                cn += 1
                
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    push(g, st, r + dx, c + dy)
                    
            return max(mx, cn)
        
        for r in range(rc):
            for c in range(cc):
                mx = dfs(g, r, c, mx)
        
        return mx
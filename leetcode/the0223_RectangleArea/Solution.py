class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        def intersect(a0, b0, a1, b1):
            if a1 >= b0 or b1 <= a0: return 0
            
            return min(b0, b1) - max(a0, a1)
        
        area1 = abs(A - C) * abs(B - D)
        area2 = abs(G - E) * abs(H - F)
        
        area_intersect = intersect(A, C, E, G) * intersect(B, D, F, H)
        
        return area1 + area2 - area_intersect
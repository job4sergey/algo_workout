class Solution(object):
    @staticmethod
    def intersect(x11, y11, x12, y12, x21, y21, x22, y22):
        max_x1 = max(x11, x12)
        max_x2 = max(x21, x22)
        min_x1 = min(x11, x12)
        min_x2 = min(x21, x22)
        dx = max(max_x1, max_x2) - min(min_x1, min_x2) - abs(max_x1 - max_x2) - abs(min_x1 - min_x2)
        if dx <= 0:
            return 0

        max_y1 = max(y11, y12)
        max_y2 = max(y21, y22)
        min_y1 = min(y11, y12)
        min_y2 = min(y21, y22)
        dy = max(max_y1, max_y2) - min(min_y1, min_y2) - abs(max_y1 - max_y2) - abs(min_y1 - min_y2)
        if dy <= 0:
            return 0

        return dx * dy

    def computeArea(self, x11, y11, x12, y12, x21, y21, x22, y22):
        return abs(x11 - x12) * abs(y11 - y12) + abs(x21 - x22) * abs(y21 - y22) \
               - self.intersect(x11, y11, x12, y12,
                                x21, y21, x22, y22)

# Idea:
# Lets encode paths in the tree as some number, its binary form meaning:
# 1 means we take the right pointer
# 0 - we take the left pointer
# Then our search space is all numbers from 000...0 to 111..1 (in binary form).
# with length of binary sequence equals tree height.
#
# Using binary search, we are going to find the path leading us to the rightmost leaf
# Note, if some path is represented as number, then to add -1 has meaning of taking its left sibling leaf.
class Solution:
    def countNodes(self, r):
        if not r:
            return 0

        h = -1  # height of the tree

        n = r  # we are going to calculate the height of the tree
        while n is not None:
            h += 1
            n = n.left

        C = (1 << h)  # the omnipresent constant
        fro = 0  # all left turns
        to = C - 1  # all right turns

        # this binary search will find path to the leftmost None leaf
        while fro <= to:
            m = to + (fro - to) // 2
            n = r
            i = C >> 1
            while i > 0:
                n = n.right if i & m else n.left
                i = i >> 1

            if n:
                fro = m + 1
            else:
                to = m - 1

        # number of nodes in the complete tree (with height = h - 1) formed by all vertices except the leaf vertices
        # What is left now is to count the number of leaves
        cn = (1 << h) - 1

        i = C >> 1
        m = fro - 1  # path to the rightmost leaf
        while i > 0:
            if i & m:
                # every time we take the right turn
                # we count the number of leaves in the (skipped) left subtree
                cn += 1 << (h - 1)
            i = i >> 1
            h -= 1

        return cn + 1  # plus one because we need to count the last leaf as well

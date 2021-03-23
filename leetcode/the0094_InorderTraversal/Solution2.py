class Solution(object):
    def inorderTraversal(self, root):
        r = root
        st = []
        res = []

        while r or st:
            while r:
                st.append(r)
                r = r.left

            r = st.pop()
            res.append(r.val)
            r = r.right

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

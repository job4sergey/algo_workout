class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        st = [root]
        res = []
        while st:
            r = st.pop()
            res.append(r.val)

            if r.right:
                st.append(r.right)

            if r.left:
                st.append(r.left)

        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

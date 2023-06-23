# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return []
        dq = collections.deque([(root)])
        while dq:
            node = dq.popleft()
            if node.val == val: return node
            if node.right: dq.append(node.right)
            if node.left: dq.append(node.left)
class Solution:
    def LCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        
        while True:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
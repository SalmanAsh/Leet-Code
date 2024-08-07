class Solution:
    res = 0
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            #Compute max with splitting
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
    
    dfs(root)
    return res[0]
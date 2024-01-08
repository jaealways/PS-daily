# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
tree에서 low와 high 사이값에 있으면 dfs 들어가고, 아니면 return
들어가면서 총 합 구하기


"""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            answer=0
            if low<=node.val<=high:
                answer+=node.val
            answer+=dfs(node.left)
            answer+=dfs(node.right)

            return answer
        
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
제일 끝 노드 즉, 다음 노드가 none이거나 null이면 이전 값 추가

"""

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        answer1,answer2=[],[]
        def dfs(node,answer):            
            if not node:
                return answer
            if not node.left and not node.right:
                answer.append(node.val)
            answer=dfs(node.left,answer)
            answer=dfs(node.right,answer)
            return answer

        return dfs(root1,answer1)==dfs(root2,answer2)

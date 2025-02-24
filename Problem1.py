# 515. Find Largest Value in Each Tree Row

# Time Complexity: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# BFS  Intuition:
# Use a queue to traverse the tree level by level.
# Keep track of the largest value in each row.
# Return the largest value in each row.

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]: 
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            max_val = float('-inf')
            for _ in range(size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_val)
        return result
    
# DFS Intuition:
# Use a recursive function to traverse the tree.
# Keep track of the largest value in each row.
# Return the largest value in each row.

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]: 
        if not root:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root, level):
        if not root:
            return
        if len(self.result) == level:
            self.result.append(root.val)
        else:
            self.result[level] = max(self.result[level], root.val)  
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
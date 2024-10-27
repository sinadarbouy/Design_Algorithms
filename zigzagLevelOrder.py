# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
      if root == None or root.val == None:
        return result
      
      result = []
      to_check = [root]
      
      left_to_right= True
      while to_check:
        level_size = len(to_check)
        level = []
        
        for _ in range(level_size):
            node = to_check.pop(0)
            level.append(node.val)
            
            if node.left:
                to_check.append(node.left)
            if node.right:
                to_check.append(node.right)
        
        if not left_to_right:
            level.reverse()
        
        result.append(level)
        left_to_right = not left_to_right
      return result

# Helper function to insert nodes in level-order
from collections import deque

def build_tree_from_list(lst):
    if not lst or lst[0] is None:
        return None
    
    # Initialize the root of the tree
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        current = queue.popleft()
        
        # Left child
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    
    return root

root_list = [1,2,3,4,None,None,5]

# Build the tree
root = build_tree_from_list(root_list)

# Create an instance of the Solution class
solution = Solution()

# Test zigzagLevelOrder
print("zigzagLevelOrder Output:", solution.zigzagLevelOrder(root))

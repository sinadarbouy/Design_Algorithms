
#Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def _inorder(node: TreeNode):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
            else:
                return
                
        _inorder(root)
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

# Test data: root = [1,2,3,4,5,null,8,null,null,6,7,9]
root_list = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]


# Build the tree
root = build_tree_from_list(root_list)

# Create an instance of the Solution class
solution = Solution()

# Test inorderTraversal
print("Inorder Traversal Output:", solution.inorderTraversal(root))

"""
================================================================
TOPIC 9: TREES (Binary Tree & BST) - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A TREE?
================================================================

A Tree is a HIERARCHICAL data structure.
Unlike arrays/linked lists (linear), trees branch out.

Real-world examples:
  - File system (folders and files)
  - Organization chart (CEO -> VPs -> Managers -> Employees)
  - HTML DOM (html -> head, body -> div, p, etc.)
  - Family tree

TERMINOLOGY:
  
          1          <-- ROOT (topmost node, no parent)
         / \
        2   3        <-- 2 and 3 are CHILDREN of 1
       / \   \            1 is the PARENT of 2 and 3
      4   5   6      <-- 4,5 are children of 2; 6 is child of 3
     /                    4,5,6 are LEAF nodes (no children)
    7                     7 is child of 4

  - ROOT: Top node (1). Every tree has exactly one root.
  - PARENT: Node directly above. (2 is parent of 4 and 5)
  - CHILD: Node directly below. (4 and 5 are children of 2)
  - LEAF: Node with NO children. (5, 6, 7)
  - EDGE: Connection between parent and child.
  - DEPTH: Distance from root. (Root=0, 2=1, 4=2, 7=3)
  - HEIGHT: Distance from node to deepest leaf below it.
  - SUBTREE: Any node and all its descendants.


================================================================
SECTION 2: BINARY TREE
================================================================

A Binary Tree is a tree where each node has AT MOST 2 children:
  - Left child
  - Right child

         1
        / \
       2   3       <-- Each node has 0, 1, or 2 children
      / \
     4   5

Types of Binary Trees:
  - FULL: Every node has 0 or 2 children (never 1)
  - COMPLETE: All levels filled except possibly last, filled left to right
  - PERFECT: All levels completely filled (2^h - 1 nodes at height h)
  - BALANCED: Height of left and right subtrees differ by at most 1


================================================================
SECTION 3: IMPLEMENTING A BINARY TREE IN PYTHON
================================================================
"""

from collections import deque


class TreeNode:
    """A node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree_from_list(values):
    """
    Build a binary tree from a list (level-order).
    None means no node at that position.
    
    [1, 2, 3, 4, 5, None, 6] builds:
           1
          / \
         2   3
        / \   \
       4   5   6
    """
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


"""
================================================================
SECTION 4: TREE TRAVERSALS (Most Important Topic!)
================================================================

Traversal = visiting every node in a specific order.
There are 4 main traversals. You MUST know all of them.

Given tree:
         1
        / \
       2   3
      / \
     4   5

1. INORDER (Left, Root, Right):   4, 2, 5, 1, 3
2. PREORDER (Root, Left, Right):  1, 2, 4, 5, 3
3. POSTORDER (Left, Right, Root): 4, 5, 2, 3, 1
4. LEVEL ORDER (BFS):             1, 2, 3, 4, 5

MEMORY TRICK:
  - INorder:   Root in the MIDDLE   (Left, ROOT, Right)
  - PREorder:  Root comes FIRST     (ROOT, Left, Right)
  - POSTorder: Root comes LAST      (Left, Right, ROOT)
"""


# --- INORDER TRAVERSAL (Left, Root, Right) ---
def inorder(root):
    """
    Visit left subtree, then root, then right subtree.
    
    For BST: Inorder gives SORTED order!
    
         1
        / \
       2   3       Inorder: 4 -> 2 -> 5 -> 1 -> 3
      / \
     4   5
    """
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# --- PREORDER TRAVERSAL (Root, Left, Right) ---
def preorder(root):
    """
    Visit root first, then left subtree, then right subtree.
    
    Useful for: copying a tree, prefix expression
    
         1
        / \
       2   3       Preorder: 1 -> 2 -> 4 -> 5 -> 3
      / \
     4   5
    """
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


# --- POSTORDER TRAVERSAL (Left, Right, Root) ---
def postorder(root):
    """
    Visit left subtree, right subtree, then root.
    
    Useful for: deleting a tree, postfix expression
    
         1
        / \
       2   3       Postorder: 4 -> 5 -> 2 -> 3 -> 1
      / \
     4   5
    """
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# --- LEVEL ORDER TRAVERSAL (BFS) ---
def level_order(root):
    """
    Visit level by level, left to right. Uses a QUEUE.
    
         1
        / \
       2   3       Level Order: [1], [2, 3], [4, 5]
      / \
     4   5
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# TIME: O(n) for all traversals
# SPACE: O(h) for recursive (h = height), O(n) for level order


"""
================================================================
SECTION 5: COMMON TREE PROBLEMS (Interview Favorites)
================================================================
"""


# ============================================================
# PROBLEM 1: Maximum Depth / Height of Binary Tree (LeetCode 104)
# ============================================================
"""
PROBLEM:
  Find the maximum depth (number of nodes on longest root-to-leaf path).
  
         3
        / \
       9  20       Depth = 3 (path: 3 -> 20 -> 7)
         / \
        15  7

APPROACH:
  Depth of a node = 1 + max(depth of left, depth of right)
  Base case: empty node has depth 0
"""

def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)

# TIME: O(n), SPACE: O(h)


# ============================================================
# PROBLEM 2: Invert Binary Tree (LeetCode 226)
# ============================================================
"""
PROBLEM: Mirror/flip the tree.
  
  Input:       4            Output:      4
              / \                       / \
             2   7                     7   2
            / \ / \                   / \ / \
           1  3 6  9                 9  6 3  1

APPROACH: Swap left and right children, then recurse.
"""

def invert_tree(root):
    if root is None:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recurse on both subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# TIME: O(n), SPACE: O(h)


# ============================================================
# PROBLEM 3: Check if Two Trees are Same (LeetCode 100)
# ============================================================

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


# ============================================================
# PROBLEM 4: Check if Tree is Symmetric (LeetCode 101)
# ============================================================
"""
PROBLEM: Is the tree a mirror of itself?

         1
        / \
       2   2       Symmetric!
      / \ / \
     3  4 4  3
"""

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    return is_mirror(root.left, root.right)


# ============================================================
# PROBLEM 5: Path Sum (LeetCode 112)
# ============================================================
"""
PROBLEM: Does any root-to-leaf path have sum equal to target?

         5
        / \
       4   8       target = 22
      /   / \      Path: 5 -> 4 -> 11 -> 2 = 22 -> True
     11  13  4
    / \       \
   7   2       1
"""

def has_path_sum(root, target_sum):
    if not root:
        return False
    
    # If it's a leaf node, check if remaining sum matches
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Check left or right subtree with reduced target
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


# ============================================================
# PROBLEM 6: Lowest Common Ancestor (LeetCode 236)
# ============================================================
"""
PROBLEM:
  Find the lowest (deepest) node that is an ancestor of both p and q.
  
         3
        / \
       5   1       LCA of 5 and 1 = 3
      / \ / \      LCA of 5 and 4 = 5
     6  2 0  8     LCA of 6 and 4 = 5
       / \
      7   4
"""

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root    # p and q are on different sides
    return left if left else right


"""
================================================================
SECTION 6: BINARY SEARCH TREE (BST)
================================================================

A BST is a binary tree with a special ORDERING property:
  - Left subtree contains only nodes with values LESS than root
  - Right subtree contains only nodes with values GREATER than root
  - Both left and right subtrees are also BSTs

         8
        / \
       3   10      This is a valid BST!
      / \    \     Everything left of 8 is < 8
     1   6    14   Everything right of 8 is > 8
        / \   /
       4   7 13

KEY PROPERTY: Inorder traversal of BST gives SORTED order!
  Inorder: 1, 3, 4, 6, 7, 8, 10, 13, 14  (sorted!)

BST OPERATIONS:
  Search: O(h) where h = height (O(log n) if balanced)
  Insert: O(h)
  Delete: O(h)
"""


# --- BST Search ---
def bst_search(root, target):
    """
    Search for a value in BST.
    If target < root -> go left
    If target > root -> go right
    """
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)

# TIME: O(h), O(log n) if balanced


# --- BST Insert ---
def bst_insert(root, val):
    """Insert a value into BST."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


# --- Validate BST (LeetCode 98) ---
def is_valid_bst(root):
    """
    Check if tree is a valid BST.
    Each node must be within a valid range.
    """
    def helper(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (helper(node.left, min_val, node.val) and
                helper(node.right, node.val, max_val))
    
    return helper(root, float('-inf'), float('inf'))


# --- Kth Smallest Element in BST (LeetCode 230) ---
def kth_smallest(root, k):
    """
    Inorder traversal gives sorted order.
    The kth element in inorder is the kth smallest.
    """
    result = []
    
    def inorder_collect(node):
        if node and len(result) < k:
            inorder_collect(node.left)
            result.append(node.val)
            inorder_collect(node.right)
    
    inorder_collect(root)
    return result[k - 1]


"""
================================================================
SUMMARY
================================================================

BINARY TREE:
  - Hierarchical structure, each node has at most 2 children
  - 4 traversals: Inorder, Preorder, Postorder, Level Order
  - Most problems solved with RECURSION

BST:
  - Left < Root < Right (ordering property)
  - Inorder = sorted order
  - Search/Insert/Delete: O(log n) if balanced

COMMON INTERVIEW PROBLEMS:
  - Max depth, Invert tree, Same tree, Symmetric tree
  - Path sum, Level order traversal
  - Validate BST, LCA, Kth smallest
  - Serialize/Deserialize tree
"""


# ============================================================
# RUN ALL EXAMPLES
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TREE EXAMPLES")
    print("=" * 60)
    
    # Build tree:    1
    #               / \
    #              2   3
    #             / \
    #            4   5
    root = build_tree_from_list([1, 2, 3, 4, 5])
    
    print("\n--- Traversals ---")
    print(f"Inorder:     {inorder(root)}")      # [4, 2, 5, 1, 3]
    print(f"Preorder:    {preorder(root)}")      # [1, 2, 4, 5, 3]
    print(f"Postorder:   {postorder(root)}")     # [4, 5, 2, 3, 1]
    print(f"Level Order: {level_order(root)}")   # [[1], [2, 3], [4, 5]]
    
    print("\n--- Max Depth ---")
    print(f"Max depth: {max_depth(root)}")       # 3
    
    print("\n--- Symmetric Check ---")
    sym_root = build_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    print(f"Is symmetric: {is_symmetric(sym_root)}")  # True
    
    print("\n--- BST Operations ---")
    # Build BST: 8, 3, 10, 1, 6, 14
    bst = None
    for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst = bst_insert(bst, val)
    
    print(f"BST Inorder (sorted): {inorder(bst)}")
    print(f"Is valid BST: {is_valid_bst(bst)}")
    print(f"Search 6: {bst_search(bst, 6)}")
    print(f"Search 99: {bst_search(bst, 99)}")
    print(f"3rd smallest: {kth_smallest(bst, 3)}")
    
    print("\nDone! Trees complete!")

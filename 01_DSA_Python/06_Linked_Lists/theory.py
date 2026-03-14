"""
================================================================
TOPIC 6: LINKED LISTS — Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A LINKED LIST?
================================================================

A Linked List is a chain of NODES where each node contains:
  1. DATA (the value)
  2. POINTER (reference to the next node)

Think of it like a TREASURE HUNT:
  - Each clue (node) has a message (data) and tells you
    where the NEXT clue is (pointer).
  - The last clue says "THE END" (points to None/null).

VISUAL:

  Head
   ↓
  [10 | →] → [20 | →] → [30 | →] → [40 | None]
  
  Each box is a NODE:
    [10 | →]  means: data = 10, next = pointer to next node

  Head = the FIRST node (our entry point)
  The last node's "next" points to None (end of list)


================================================================
SECTION 2: LINKED LIST vs ARRAY — WHY DO WE NEED IT?
================================================================

ARRAY (Python List):
  +-----+-----+-----+-----+-----+
  | 10  | 20  | 30  | 40  | 50  |    ← Contiguous memory
  +-----+-----+-----+-----+-----+
  
  ✓ Fast access by index: O(1)
  ✗ Slow insertion/deletion in middle: O(n) — must shift elements
  ✗ Fixed size (or expensive resize)

LINKED LIST:
  [10|→] → [20|→] → [30|→] → [40|→] → [50|None]
  
  ✗ Slow access by index: O(n) — must traverse from head
  ✓ Fast insertion/deletion at known position: O(1) — just change pointers
  ✓ Dynamic size — grows/shrinks easily

WHEN TO USE LINKED LIST:
  - Frequent insertions/deletions at beginning or middle
  - Don't need random access by index
  - Implementing stacks, queues, LRU cache


================================================================
SECTION 3: TYPES OF LINKED LISTS
================================================================

1. SINGLY LINKED LIST (Most Common in Interviews)
   Each node points to the NEXT node only.
   [10|→] → [20|→] → [30|None]
   Can only go FORWARD.

2. DOUBLY LINKED LIST
   Each node has pointers to BOTH next and previous.
   None ← [←|10|→] ↔ [←|20|→] ↔ [←|30|→] → None
   Can go FORWARD and BACKWARD.

3. CIRCULAR LINKED LIST
   Last node points back to the first node.
   [10|→] → [20|→] → [30|→] → (back to [10])

We'll focus on SINGLY LINKED LIST first.


================================================================
SECTION 4: IMPLEMENTING A LINKED LIST IN PYTHON
================================================================
"""


# ============================================================
# STEP 1: Define the Node class
# ============================================================
class ListNode:
    """
    A single node in a linked list.
    
    Each node stores:
      - val: the data value
      - next: reference to the next node (or None if last)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


# ============================================================
# STEP 2: Helper function to create a linked list from a list
# ============================================================
def create_linked_list(arr):
    """
    Convert a Python list to a linked list.
    
    [1, 2, 3] → 1 → 2 → 3 → None
    
    VISUAL (step by step):
      Start with arr = [1, 2, 3]
      
      Create dummy head: [dummy|→] → None
      
      Add 1: [dummy|→] → [1|None]
      Add 2: [dummy|→] → [1|→] → [2|None]
      Add 3: [dummy|→] → [1|→] → [2|→] → [3|None]
      
      Return dummy.next = [1|→] → [2|→] → [3|None]
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head


# ============================================================
# STEP 3: Helper function to print a linked list
# ============================================================
def print_linked_list(head):
    """Print linked list in readable format."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" → ".join(values) + " → None")


# ============================================================
# SECTION 5: BASIC OPERATIONS
# ============================================================

# --- Operation 1: Traversal (Visit every node) ---
def traverse(head):
    """
    Go through every node from head to end.
    This is the MOST BASIC operation.
    
    VISUAL:
      1 → 2 → 3 → None
      ↑
      current (start here)
      
      Step 1: current = 1, print 1, move to next
      Step 2: current = 2, print 2, move to next  
      Step 3: current = 3, print 3, move to next
      Step 4: current = None → STOP
    """
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next     # move to next node
    print()

# TIME: O(n) — visit every node once


# --- Operation 2: Find Length ---
def get_length(head):
    """Count the number of nodes."""
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# TIME: O(n)


# --- Operation 3: Search for a Value ---
def search(head, target):
    """
    Return True if target exists in the linked list.
    
    VISUAL: Search for 3 in: 1 → 2 → 3 → 4 → None
      current=1: 1==3? No → move
      current=2: 2==3? No → move
      current=3: 3==3? YES → return True
    """
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False

# TIME: O(n)


# --- Operation 4: Insert at Beginning ---
def insert_at_beginning(head, val):
    """
    Add a new node at the BEGINNING.
    
    VISUAL: Insert 0 at beginning of: 1 → 2 → 3 → None
    
      Step 1: Create new node [0|None]
      Step 2: Point new node to current head: [0|→] → 1 → 2 → 3 → None
      Step 3: Update head to new node
      
      Result: 0 → 1 → 2 → 3 → None
    """
    new_node = ListNode(val)
    new_node.next = head    # point new node to current head
    return new_node         # new node is the new head

# TIME: O(1) — just changing pointers!


# --- Operation 5: Insert at End ---
def insert_at_end(head, val):
    """
    Add a new node at the END.
    Must traverse to find the last node first.
    """
    new_node = ListNode(val)
    
    if not head:  # empty list
        return new_node
    
    current = head
    while current.next:       # go to last node
        current = current.next
    current.next = new_node   # attach new node at end
    
    return head

# TIME: O(n) — must traverse to end


# --- Operation 6: Delete a Node by Value ---
def delete_node(head, val):
    """
    Delete the FIRST node with the given value.
    
    VISUAL: Delete 3 from: 1 → 2 → 3 → 4 → None
    
      Find node BEFORE 3 (which is 2)
      Change 2's next to skip 3: 2.next = 3.next = 4
      
      Result: 1 → 2 → 4 → None
      
      The node [3|→] is now disconnected (Python garbage collects it)
    """
    # Special case: delete head node
    if head and head.val == val:
        return head.next
    
    current = head
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next  # skip the node
            return head
        current = current.next
    
    return head  # value not found

# TIME: O(n) — must search for the node


# ============================================================
# SECTION 6: THE DUMMY NODE TRICK (Very Important!)
# ============================================================
"""
Many linked list problems are easier if you create a DUMMY node
that points to the head. This avoids special-casing the head node.

WITHOUT dummy: You need special logic for "what if we delete the head?"
WITH dummy: Head is just another node, no special case.

    dummy → 1 → 2 → 3 → None
    
    At the end, return dummy.next (the real head)
"""


# ============================================================
# SECTION 7: COMMON INTERVIEW PATTERNS
# ============================================================

# --- Pattern 1: Reverse a Linked List (LeetCode 206) ---
"""
PROBLEM:
  Reverse a singly linked list.
  
  Input:  1 → 2 → 3 → 4 → 5 → None
  Output: 5 → 4 → 3 → 2 → 1 → None

APPROACH: Change the direction of each pointer.

VISUAL (step by step):
  prev=None, current=1

  Step 1: Save next (2), point 1→None, move forward
          None ← 1    2 → 3 → 4 → 5
          prev=1, current=2

  Step 2: Save next (3), point 2→1, move forward
          None ← 1 ← 2    3 → 4 → 5
          prev=2, current=3

  Step 3: Save next (4), point 3→2, move forward
          None ← 1 ← 2 ← 3    4 → 5
          prev=3, current=4

  Step 4: Save next (5), point 4→3, move forward
          None ← 1 ← 2 ← 3 ← 4    5
          prev=4, current=5

  Step 5: Save next (None), point 5→4, move forward
          None ← 1 ← 2 ← 3 ← 4 ← 5
          prev=5, current=None → STOP

  Return prev (5) → 5 → 4 → 3 → 2 → 1 → None ✓
"""

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # save next (before we lose it!)
        current.next = prev       # reverse the pointer
        prev = current            # move prev forward
        current = next_node       # move current forward
    
    return prev  # prev is the new head

# TIME: O(n), SPACE: O(1)


# --- Pattern 2: Find Middle of Linked List (LeetCode 876) ---
"""
PROBLEM:
  Find the middle node. If two middles, return the second one.
  
  Input:  1 → 2 → 3 → 4 → 5 → None
  Output: Node 3
  
  Input:  1 → 2 → 3 → 4 → 5 → 6 → None
  Output: Node 4 (second middle)

APPROACH: Slow & Fast Pointers (Tortoise and Hare)
  - Slow moves 1 step, Fast moves 2 steps.
  - When fast reaches end, slow is at middle!

VISUAL:
  1 → 2 → 3 → 4 → 5 → None
  S   F                        → slow=1, fast=1
      S       F                → slow=2, fast=3
          S           F        → slow=3, fast=5
                                 fast.next=None → STOP
  Slow is at 3 = MIDDLE ✓
"""

def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
    
    return slow  # slow is at middle

# TIME: O(n), SPACE: O(1)


# --- Pattern 3: Detect Cycle (LeetCode 141) ---
"""
PROBLEM:
  Determine if a linked list has a CYCLE (loop).
  
  1 → 2 → 3 → 4
          ↑       ↓
          6 ← 5     ← This is a cycle!
  
APPROACH: Floyd's Cycle Detection (Tortoise and Hare)
  - Slow moves 1 step, Fast moves 2 steps.
  - If there's a cycle, fast will eventually CATCH slow.
  - If no cycle, fast reaches None.

  Think of it like two runners on a circular track:
  The faster one will eventually lap the slower one.
"""

def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:      # they met → cycle exists!
            return True
    
    return False  # fast reached end → no cycle

# TIME: O(n), SPACE: O(1)


# --- Pattern 4: Merge Two Sorted Lists (LeetCode 21) ---
"""
PROBLEM:
  Merge two sorted linked lists into one sorted list.
  
  Input:  1 → 2 → 4 → None
          1 → 3 → 4 → None
  Output: 1 → 1 → 2 → 3 → 4 → 4 → None

APPROACH: Use dummy node, compare heads, pick smaller.

VISUAL:
  List1: 1 → 2 → 4
  List2: 1 → 3 → 4
  
  dummy → ?
  
  Compare 1 vs 1: pick List1's 1 → dummy → 1
  Compare 2 vs 1: pick List2's 1 → dummy → 1 → 1
  Compare 2 vs 3: pick List1's 2 → dummy → 1 → 1 → 2
  Compare 4 vs 3: pick List2's 3 → dummy → 1 → 1 → 2 → 3
  Compare 4 vs 4: pick List1's 4 → dummy → 1 → 1 → 2 → 3 → 4
  List1 done, append rest of List2 → dummy → 1 → 1 → 2 → 3 → 4 → 4
"""

def merge_two_lists(l1, l2):
    dummy = ListNode(0)     # dummy node to simplify logic
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next  # skip dummy, return real head

# TIME: O(n + m), SPACE: O(1) — reusing existing nodes


# --- Pattern 5: Remove Nth Node From End (LeetCode 19) ---
"""
PROBLEM:
  Remove the nth node from the END of the list.
  
  Input:  1 → 2 → 3 → 4 → 5 → None, n = 2
  Output: 1 → 2 → 3 → 5 → None  (removed 4, which is 2nd from end)

APPROACH: Two Pointers with Gap
  1. Move fast pointer n steps ahead
  2. Move both pointers together until fast reaches end
  3. Now slow is right BEFORE the node to delete

VISUAL (n=2):
  dummy → 1 → 2 → 3 → 4 → 5 → None
  
  Move fast 2 steps ahead:
  slow=dummy, fast=2
  
  Move together:
  slow=1, fast=3
  slow=2, fast=4
  slow=3, fast=5
  fast.next=None → STOP
  
  Delete slow.next (4): slow.next = slow.next.next
  Result: 1 → 2 → 3 → 5 → None ✓
"""

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    # Move fast n+1 steps ahead (so slow lands BEFORE target)
    for _ in range(n + 1):
        fast = fast.next
    
    # Move together
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Delete the node
    slow.next = slow.next.next
    
    return dummy.next

# TIME: O(n), SPACE: O(1)


# ============================================================
# RUN ALL EXAMPLES
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("LINKED LIST EXAMPLES")
    print("=" * 60)
    
    # Create a linked list
    print("\n--- Create & Print ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(head)  # 1 → 2 → 3 → 4 → 5 → None
    
    # Basic operations
    print("\n--- Basic Operations ---")
    print(f"Length: {get_length(head)}")           # 5
    print(f"Search 3: {search(head, 3)}")          # True
    print(f"Search 99: {search(head, 99)}")        # False
    
    # Insert at beginning
    print("\n--- Insert at Beginning ---")
    head = insert_at_beginning(head, 0)
    print_linked_list(head)  # 0 → 1 → 2 → 3 → 4 → 5 → None
    
    # Insert at end
    print("\n--- Insert at End ---")
    head = insert_at_end(head, 6)
    print_linked_list(head)  # 0 → 1 → 2 → 3 → 4 → 5 → 6 → None
    
    # Delete node
    print("\n--- Delete Node (value=3) ---")
    head = delete_node(head, 3)
    print_linked_list(head)  # 0 → 1 → 2 → 4 → 5 → 6 → None
    
    # Reverse
    print("\n--- Reverse ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    head = reverse_linked_list(head)
    print_linked_list(head)  # 5 → 4 → 3 → 2 → 1 → None
    
    # Find Middle
    print("\n--- Find Middle ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    mid = find_middle(head)
    print(f"Middle of [1,2,3,4,5]: {mid.val}")  # 3
    
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    mid = find_middle(head)
    print(f"Middle of [1,2,3,4,5,6]: {mid.val}")  # 4
    
    # Merge Two Sorted Lists
    print("\n--- Merge Two Sorted Lists ---")
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(l1, l2)
    print_linked_list(merged)  # 1 → 1 → 2 → 3 → 4 → 4 → None
    
    # Remove Nth from End
    print("\n--- Remove 2nd from End ---")
    head = create_linked_list([1, 2, 3, 4, 5])
    head = remove_nth_from_end(head, 2)
    print_linked_list(head)  # 1 → 2 → 3 → 5 → None
    
    print("\n✅ Linked List theory complete!")

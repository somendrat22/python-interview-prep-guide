"""
================================================================
TOPIC 7: STACKS & QUEUES — Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A STACK?
================================================================

A Stack is a data structure that follows LIFO — Last In, First Out.

Think of it like a STACK OF PLATES:
  - You can only add a plate on TOP (push)
  - You can only remove the plate on TOP (pop)
  - You can't pull a plate from the middle!

    TOP →  | 30 |   ← Last added, First removed
           | 20 |
           | 10 |   ← First added, Last removed
           +----+

Operations:
  push(x)  — Add element to top      O(1)
  pop()    — Remove & return top      O(1)
  peek()   — Look at top without removing  O(1)
  isEmpty()— Check if stack is empty  O(1)

Real-world examples of stacks:
  - Browser back button (pages visited)
  - Undo/Redo in text editors
  - Function call stack in programming
  - Balancing parentheses in code


================================================================
SECTION 2: IMPLEMENTING A STACK IN PYTHON
================================================================

Python's list works perfectly as a stack!
  - append() = push (add to top)
  - pop() = pop (remove from top)
  Both are O(1)!
"""


# ============================================================
# Stack using Python list
# ============================================================
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item. Raises error if empty."""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items."""
        return len(self.items)
    
    def __repr__(self):
        return f"Stack({self.items})"


# Quick demo
print("=== Stack Demo ===")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(f"Stack: {s}")              # Stack([10, 20, 30])
print(f"Peek: {s.peek()}")       # 30 (top element)
print(f"Pop: {s.pop()}")         # 30 (removed from top)
print(f"Stack after pop: {s}")   # Stack([10, 20])

# Even simpler — just use a list directly:
# stack = []
# stack.append(10)   # push
# stack.pop()        # pop
# stack[-1]          # peek


"""
================================================================
SECTION 3: WHAT IS A QUEUE?
================================================================

A Queue follows FIFO — First In, First Out.

Think of it like a LINE AT A STORE:
  - People join at the BACK (enqueue)
  - People leave from the FRONT (dequeue)
  - First person in line gets served first

    FRONT                    BACK
    [10] ← [20] ← [30] ← [40]
     ↑ dequeue          enqueue ↑
     (remove from here)  (add here)

Operations:
  enqueue(x)  — Add to back       O(1)
  dequeue()   — Remove from front  O(1)
  peek()      — Look at front      O(1)
  isEmpty()   — Check if empty     O(1)

Real-world examples of queues:
  - Printer queue (first document prints first)
  - Task scheduling in OS
  - BFS in graphs (uses a queue!)
  - Message queues (Kafka, RabbitMQ)


================================================================
SECTION 4: IMPLEMENTING A QUEUE IN PYTHON
================================================================

IMPORTANT: Do NOT use a regular list for queues!
  list.pop(0) is O(n) because it shifts all elements.
  
  Instead use collections.deque (double-ended queue):
  - deque.append() = enqueue (add to back)    O(1)
  - deque.popleft() = dequeue (remove from front)  O(1)
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to back of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.popleft()
    
    def peek(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Queue({list(self.items)})"


# Quick demo
print("\n=== Queue Demo ===")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(f"Queue: {q}")               # Queue([10, 20, 30])
print(f"Peek: {q.peek()}")         # 10 (front element)
print(f"Dequeue: {q.dequeue()}")   # 10 (removed from front)
print(f"Queue after dequeue: {q}") # Queue([20, 30])

# Even simpler — just use deque directly:
# q = deque()
# q.append(10)      # enqueue
# q.popleft()       # dequeue
# q[0]              # peek


"""
================================================================
SECTION 5: STACK — CLASSIC INTERVIEW PROBLEMS
================================================================
"""


# ============================================================
# PROBLEM 1: Valid Parentheses (LeetCode 20) — MUST KNOW!
# ============================================================
"""
PROBLEM:
  Check if a string of brackets is valid.
  Valid means: every open bracket has a matching close bracket in correct order.
  
  Input:  "()"      → True
  Input:  "()[]{}"  → True
  Input:  "(]"      → False
  Input:  "([)]"    → False
  Input:  "{[]}"    → True

WHY USE A STACK?
  When we see an opening bracket, we expect a matching closing bracket LATER.
  Stack stores what we're "expecting" — LIFO matches the nesting!

VISUAL:
  s = "{[()]}"
  
  '{' → push → stack: ['{']
  '[' → push → stack: ['{', '[']
  '(' → push → stack: ['{', '[', '(']
  ')' → matches '(' on top → pop → stack: ['{', '[']
  ']' → matches '[' on top → pop → stack: ['{']
  '}' → matches '{' on top → pop → stack: []
  
  Stack empty at end → VALID ✓
"""

def is_valid_parentheses(s):
    stack = []
    # Map closing brackets to their matching opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map:   # it's a closing bracket
            # Check if top of stack has matching opening bracket
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:                      # it's an opening bracket
            stack.append(char)
    
    return len(stack) == 0  # stack should be empty if all matched

# TIME: O(n), SPACE: O(n)


# ============================================================
# PROBLEM 2: Min Stack (LeetCode 155)
# ============================================================
"""
PROBLEM:
  Design a stack that supports push, pop, top, and getMin in O(1).

APPROACH:
  Maintain TWO stacks:
    1. Regular stack for normal operations
    2. Min stack that tracks the current minimum
  
  When pushing: if new value <= current min, push to min stack too
  When popping: if popped value == current min, pop from min stack too
  
  Actually, SIMPLER approach: push (value, current_min) tuples.
"""

class MinStack:
    def __init__(self):
        self.stack = []  # stores (value, current_minimum) tuples
    
    def push(self, val):
        if self.stack:
            current_min = min(val, self.stack[-1][1])
        else:
            current_min = val
        self.stack.append((val, current_min))
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]

# All operations: O(1) time, O(n) space


# ============================================================
# PROBLEM 3: Next Greater Element (Classic Stack Problem)
# ============================================================
"""
PROBLEM:
  For each element, find the NEXT element that is GREATER than it.
  If no greater element exists, output -1.
  
  Input:  [4, 5, 2, 10, 8]
  Output: [5, 10, 10, -1, -1]
  
  Explanation:
    4 → next greater is 5
    5 → next greater is 10
    2 → next greater is 10
    10 → no greater element → -1
    8 → no greater element → -1

APPROACH: Monotonic Stack (Stack that maintains decreasing order)
  - Traverse from RIGHT to LEFT
  - Stack keeps elements in decreasing order
  - For each element, pop elements smaller than it (they can't be "next greater" for anyone)
  - Top of stack is the answer

VISUAL:
  arr = [4, 5, 2, 10, 8], traverse right to left
  
  i=4: num=8,  stack=[]      → answer=-1, push 8.  stack=[8]
  i=3: num=10, stack=[8]     → 8<10, pop. stack=[] → answer=-1, push 10. stack=[10]
  i=2: num=2,  stack=[10]    → 10>2 → answer=10, push 2. stack=[10,2]
  i=1: num=5,  stack=[10,2]  → 2<5, pop. 10>5 → answer=10, push 5. stack=[10,5]
  i=0: num=4,  stack=[10,5]  → 5>4 → answer=5, push 4. stack=[10,5,4]
  
  Result: [5, 10, 10, -1, -1] ✓
"""

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stores values, maintains decreasing order
    
    for i in range(n - 1, -1, -1):  # right to left
        # Pop elements smaller than current (useless for future elements)
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # Top of stack is the next greater element
        if stack:
            result[i] = stack[-1]
        
        # Push current element
        stack.append(arr[i])
    
    return result

# TIME: O(n) — each element pushed and popped at most once
# SPACE: O(n)


# ============================================================
# PROBLEM 4: Implement Queue using Two Stacks (LeetCode 232)
# ============================================================
"""
PROBLEM:
  Implement a queue using only two stacks.

APPROACH:
  Stack 1 (inbox): for enqueue operations
  Stack 2 (outbox): for dequeue operations
  
  When dequeue is called and outbox is empty,
  pour ALL elements from inbox into outbox (reverses order!)
  
  VISUAL:
    enqueue 1, 2, 3:
      inbox:  [1, 2, 3]  (3 on top)
      outbox: []
    
    dequeue:
      outbox is empty → pour inbox into outbox
      inbox:  []
      outbox: [3, 2, 1]  (1 on top — first in!)
      
      pop from outbox → returns 1 ✓ (FIFO!)
"""

class QueueUsingStacks:
    def __init__(self):
        self.inbox = []    # for push
        self.outbox = []   # for pop
    
    def enqueue(self, x):
        self.inbox.append(x)
    
    def dequeue(self):
        if not self.outbox:
            # Pour inbox into outbox
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
    
    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]
    
    def is_empty(self):
        return not self.inbox and not self.outbox

# Amortized O(1) for all operations!


# ============================================================
# PROBLEM 5: Daily Temperatures (LeetCode 739)
# ============================================================
"""
PROBLEM:
  Given daily temperatures, for each day, how many days until a warmer day?
  
  Input:  [73, 74, 75, 71, 69, 72, 76, 73]
  Output: [1,  1,  4,  2,  1,  1,  0,  0]
  
  Day 0 (73°): next warmer is Day 1 (74°) → 1 day
  Day 2 (75°): next warmer is Day 6 (76°) → 4 days
  Day 6 (76°): no warmer day → 0

APPROACH: Monotonic Stack (store indices)
"""

def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # stores indices of temperatures we haven't found answer for
    
    for i in range(n):
        # While current temp is warmer than temp at top of stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index  # days until warmer
        stack.append(i)
    
    return result

# TIME: O(n), SPACE: O(n)


"""
================================================================
SECTION 6: QUEUE — INTERVIEW PROBLEMS  
================================================================

Queue problems often appear in:
  - BFS (Breadth-First Search) — Topic 11 (Graphs)
  - Level-order tree traversal — Topic 9 (Trees)
  - Sliding window maximum
"""


# ============================================================
# PROBLEM 6: Implement Stack using Two Queues (LeetCode 225)
# ============================================================

class StackUsingQueues:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        # Rotate so newest element is at front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0


# ============================================================
# SUMMARY
# ============================================================
"""
STACK (LIFO):
  - Use Python list: append() = push, pop() = pop, [-1] = peek
  - Key problems: Valid Parentheses, Min Stack, Next Greater Element,
    Monotonic Stack, Expression Evaluation

QUEUE (FIFO):
  - Use collections.deque: append() = enqueue, popleft() = dequeue
  - Key problems: BFS, Level-order traversal, Sliding Window Max

WHEN TO USE STACK:
  ✓ Matching/nesting problems (parentheses, HTML tags)
  ✓ "Next greater/smaller" problems
  ✓ Undo operations
  ✓ DFS (Depth-First Search)
  ✓ Expression evaluation

WHEN TO USE QUEUE:
  ✓ BFS (Breadth-First Search)
  ✓ Level-by-level processing
  ✓ Order preservation (FIFO)
  ✓ Rate limiting, scheduling
"""


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TESTING STACK & QUEUE PROBLEMS")
    print("=" * 60)
    
    print("\n--- Valid Parentheses ---")
    print(f"'()[]{{}}' → {is_valid_parentheses('()[]{}')}")      # True
    print(f"'(]' → {is_valid_parentheses('(]')}")                 # False
    print(f"'{{[()]}}' → {is_valid_parentheses('{[()]}')}")       # True
    print(f"'([)]' → {is_valid_parentheses('([)]')}")             # False
    
    print("\n--- Min Stack ---")
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    print(f"Min: {ms.getMin()}")    # -3
    ms.pop()
    print(f"Top: {ms.top()}")       # 0
    print(f"Min: {ms.getMin()}")    # -2
    
    print("\n--- Next Greater Element ---")
    print(f"[4,5,2,10,8] → {next_greater_element([4,5,2,10,8])}")
    # [5, 10, 10, -1, -1]
    
    print("\n--- Queue using Stacks ---")
    qs = QueueUsingStacks()
    qs.enqueue(1); qs.enqueue(2); qs.enqueue(3)
    print(f"Dequeue: {qs.dequeue()}")  # 1 (FIFO!)
    print(f"Dequeue: {qs.dequeue()}")  # 2
    
    print("\n--- Daily Temperatures ---")
    print(f"[73,74,75,71,69,72,76,73] → {daily_temperatures([73,74,75,71,69,72,76,73])}")
    # [1, 1, 4, 2, 1, 1, 0, 0]
    
    print("\n✅ Stacks & Queues complete!")

"""
============================================================
TOPIC 1: TIME & SPACE COMPLEXITY (Big O Notation)
============================================================
This is the FOUNDATION of DSA. Every interview answer must
include complexity analysis.

============================================================
WHAT IS TIME COMPLEXITY?
============================================================
- Measures how the runtime of an algorithm grows as input size (n) grows.
- We use Big O notation to describe the WORST CASE.

Common Complexities (fastest → slowest):
-----------------------------------------
O(1)        → Constant      → dict lookup, array index access
O(log n)    → Logarithmic   → Binary search
O(n)        → Linear        → Single loop through array
O(n log n)  → Linearithmic  → Merge sort, Timsort (Python's sorted())
O(n²)       → Quadratic     → Nested loops (bubble sort)
O(2^n)      → Exponential   → Recursive fibonacci (naive)
O(n!)       → Factorial     → Permutations


============================================================
WHAT IS SPACE COMPLEXITY?
============================================================
- Measures how much EXTRA memory an algorithm uses.
- Does NOT count the input itself (usually).
- Includes: variables, data structures, recursion call stack.


============================================================
RULES FOR CALCULATING BIG O
============================================================
Rule 1: Drop constants        → O(2n) = O(n)
Rule 2: Drop lower order terms → O(n² + n) = O(n²)
Rule 3: Different inputs       → O(a + b) not O(n) if two different inputs
Rule 4: Nested loops multiply  → Two nested loops over n = O(n²)
Rule 5: Sequential loops add   → Two separate loops over n = O(n + n) = O(n)
"""


# ============================================================
# EXAMPLES WITH COMPLEXITY ANALYSIS
# ============================================================

# --- O(1) - Constant Time ---
def get_first_element(arr):
    """Access by index is O(1). Doesn't matter if array has 10 or 10 million elements."""
    return arr[0]  # Time: O(1), Space: O(1)


# --- O(n) - Linear Time ---
def find_max(arr):
    """Single pass through the array."""
    max_val = arr[0]
    for num in arr:        # runs n times
        if num > max_val:
            max_val = num
    return max_val
    # Time: O(n), Space: O(1)


# --- O(n²) - Quadratic Time ---
def has_duplicate_pairs(arr):
    """Nested loop = multiply."""
    n = len(arr)
    for i in range(n):           # n times
        for j in range(i+1, n):  # n times (roughly)
            if arr[i] == arr[j]:
                return True
    return False
    # Time: O(n²), Space: O(1)


# --- O(log n) - Logarithmic Time ---
def binary_search(arr, target):
    """Each step cuts the problem in HALF → log₂(n) steps."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    # Time: O(log n), Space: O(1)


# --- O(n log n) - Linearithmic Time ---
def sort_array(arr):
    """Python's built-in sort uses Timsort."""
    return sorted(arr)
    # Time: O(n log n), Space: O(n) — sorted() creates a new list


# --- O(2^n) - Exponential Time ---
def fibonacci_naive(n):
    """Each call branches into TWO more calls."""
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)
    # Time: O(2^n), Space: O(n) — recursion depth


# --- O(n) Time, O(n) Space ---
def fibonacci_optimal(n):
    """Using memoization (Dynamic Programming)."""
    memo = {}
    def helper(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]
    return helper(n)
    # Time: O(n), Space: O(n)


# ============================================================
# PYTHON-SPECIFIC COMPLEXITIES TO KNOW
# ============================================================
"""
Operation                  | Average Case | Worst Case
---------------------------|-------------|----------
list.append(x)            | O(1)*       | O(1)*     (* amortized)
list.pop()                | O(1)        | O(1)
list.pop(0)               | O(n)        | O(n)      ← AVOID! Use deque
list[i]                   | O(1)        | O(1)
list.insert(i, x)         | O(n)        | O(n)
x in list                 | O(n)        | O(n)
list.sort()               | O(n log n)  | O(n log n)
len(list)                 | O(1)        | O(1)

dict[key]                 | O(1)        | O(n)      (hash collision, rare)
dict[key] = val           | O(1)        | O(n)
key in dict               | O(1)        | O(n)
dict.keys()               | O(1)        | O(1)      (returns view)

set.add(x)                | O(1)        | O(n)
x in set                  | O(1)        | O(n)
set.union(other)          | O(len(s)+len(t))

str concatenation (+ in loop) | O(n²)   ← Use ''.join() instead → O(n)

collections.deque:
  deque.append(x)         | O(1)
  deque.appendleft(x)     | O(1)
  deque.pop()             | O(1)
  deque.popleft()         | O(1)        ← This is why deque > list for queues

heapq.heappush()          | O(log n)
heapq.heappop()           | O(log n)
heapq.heapify()           | O(n)
"""


# ============================================================
# COMMON INTERVIEW TRICK QUESTIONS
# ============================================================

# Q: What is the time complexity of this?
def trick_question_1(n):
    """Looks like O(n²) but it's actually O(n)!"""
    i = 0
    while i < n:
        j = 0
        while j < n:
            j += 1  # inner loop runs n times
            break    # BUT it breaks immediately! So inner = O(1)
        i += 1
    # Answer: O(n) because inner loop always runs once


# Q: What is the time complexity?
def trick_question_2(n):
    """Loop variable doubles each time."""
    i = 1
    count = 0
    while i < n:
        count += 1
        i *= 2  # doubles each iteration
    return count
    # Answer: O(log n) because i goes 1, 2, 4, 8, ... , n


# ============================================================
# PRACTICE PROBLEMS
# ============================================================
"""
1. Given a function, determine its Big O:
   - for i in range(n): for j in range(n): ...          → O(n²)
   - for i in range(n): for j in range(i): ...          → O(n²)  (still n²: n*(n-1)/2)
   - for i in range(n): for j in range(100): ...        → O(n)   (inner is constant)
   - while n > 0: n = n // 2                            → O(log n)

2. Which is faster for lookup: list or set? 
   → set: O(1) avg vs list: O(n)

3. Why is string concatenation in a loop O(n²)?
   → Because strings are immutable; each + creates a new string, copying all previous chars.
   → Fix: Use a list and ''.join() at the end.
"""


if __name__ == "__main__":
    # Quick demonstrations
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    print("=== O(1) - Get first element ===")
    print(f"First element: {get_first_element(arr)}")
    
    print("\n=== O(n) - Find max ===")
    print(f"Max element: {find_max(arr)}")
    
    print("\n=== O(n²) - Has duplicate pairs ===")
    print(f"Has duplicates: {has_duplicate_pairs(arr)}")
    
    print("\n=== O(log n) - Binary search ===")
    sorted_arr = sorted(arr)
    print(f"Sorted: {sorted_arr}")
    print(f"Index of 5: {binary_search(sorted_arr, 5)}")
    
    print("\n=== O(2^n) vs O(n) - Fibonacci ===")
    print(f"Fib(10) naive: {fibonacci_naive(10)}")
    print(f"Fib(10) optimal: {fibonacci_optimal(10)}")
    
    print("\n=== Trick: log n loop ===")
    print(f"Log₂(1024) iterations: {trick_question_2(1024)}")  # should be 10

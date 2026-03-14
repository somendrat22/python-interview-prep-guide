"""
================================================================
TOPIC 2: ARRAYS — Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS AN ARRAY?
================================================================

An array is a collection of items stored in CONTIGUOUS (side-by-side)
memory locations.

Think of it like a row of lockers in a school:
  - Each locker has a NUMBER (index) — 0, 1, 2, 3, ...
  - Each locker can hold ONE item (value)
  - You can directly go to locker #5 without opening lockers 0-4

    Index:   0     1     2     3     4
           +-----+-----+-----+-----+-----+
    Value: | 10  | 20  | 30  | 40  | 50  |
           +-----+-----+-----+-----+-----+
    
    arr[0] = 10
    arr[2] = 30
    arr[4] = 50
3
KEY POINTS:
  - Index starts from 0 (not 1!)
  - Last index = length - 1
  - Accessing any element by index is O(1) — instant!


================================================================
SECTION 2: ARRAYS IN PYTHON — THE "LIST"
================================================================

In Python, we don't have traditional arrays. We use LISTS.
Python lists are MORE powerful than arrays in C/Java because:
  - They can GROW and SHRINK dynamically (no fixed size)
  - They can hold DIFFERENT data types (but avoid this in interviews)

Let's learn every operation step by step:
"""


# ============================================================
# 2.1 — CREATING A LIST
# ============================================================

# Empty list
empty_list = []
print("Empty list:", empty_list)        # []

# List with values
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)              # [10, 20, 30, 40, 50]

# List of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)                # ['apple', 'banana', 'cherry']

# List with repeated values
zeros = [0] * 5
print("Zeros:", zeros)                  # [0, 0, 0, 0, 0]

# List from range
one_to_five = list(range(1, 6))
print("1 to 5:", one_to_five)           # [1, 2, 3, 4, 5]


# ============================================================
# 2.2 — ACCESSING ELEMENTS
# ============================================================
"""
Use index to access elements.
  - Positive index: left to right (0, 1, 2, ...)
  - Negative index: right to left (-1, -2, -3, ...)

    Index:     0     1     2     3     4
             +-----+-----+-----+-----+-----+
    Value:   | 10  | 20  | 30  | 40  | 50  |
             +-----+-----+-----+-----+-----+
    Neg idx:  -5    -4    -3    -2    -1
"""

arr = [10, 20, 30, 40, 50]

print("\n--- Accessing Elements ---")
print("First element (arr[0]):", arr[0])       # 10
print("Third element (arr[2]):", arr[2])       # 30
print("Last element (arr[-1]):", arr[-1])      # 50
print("Second last (arr[-2]):", arr[-2])       # 40
print("Length:", len(arr))                      # 5


# ============================================================
# 2.3 — MODIFYING ELEMENTS
# ============================================================
"""
Lists are MUTABLE — you can change values after creation.
"""

print("\n--- Modifying Elements ---")
arr = [10, 20, 30, 40, 50]
print("Before:", arr)          # [10, 20, 30, 40, 50]

arr[1] = 99                    # Change index 1 from 20 to 99
print("After arr[1]=99:", arr) # [10, 99, 30, 40, 50]


# ============================================================
# 2.4 — ADDING ELEMENTS
# ============================================================
"""
append(x)   — Add to END.             O(1)
insert(i,x) — Add at specific index.  O(n) — because it shifts everything after i
extend(lst) — Add all items of another list to end.  O(k) where k = len(lst)
"""

print("\n--- Adding Elements ---")
arr = [10, 20, 30]

# append — add to end (MOST COMMON, FAST)
arr.append(40)
print("After append(40):", arr)   # [10, 20, 30, 40]

# insert — add at specific position (SLOW for large lists)
arr.insert(1, 15)                 # Insert 15 at index 1
print("After insert(1,15):", arr) # [10, 15, 20, 30, 40]
# WHY is insert O(n)? Because everything after index 1 must shift right:
#   Before: [10, 20, 30, 40]
#                 ↓  shift right →
#   After:  [10, 15, 20, 30, 40]

# extend — add multiple items
arr.extend([50, 60])
print("After extend([50,60]):", arr)  # [10, 15, 20, 30, 40, 50, 60]


# ============================================================
# 2.5 — REMOVING ELEMENTS
# ============================================================
"""
pop()       — Remove & return LAST element.     O(1)
pop(i)      — Remove & return element at index i. O(n) — shifts elements
remove(x)   — Remove FIRST occurrence of value x. O(n) — searches then shifts
del arr[i]  — Delete element at index i.         O(n)
clear()     — Remove ALL elements.               O(1)
"""

print("\n--- Removing Elements ---")
arr = [10, 20, 30, 40, 50]

# pop — remove last (FAST)
last = arr.pop()
print(f"pop() returned {last}, arr = {arr}")      # 50, [10, 20, 30, 40]

# pop(i) — remove at index (SLOW)
second = arr.pop(1)
print(f"pop(1) returned {second}, arr = {arr}")    # 20, [10, 30, 40]

# remove — remove by value (SLOW, searches first)
arr = [10, 20, 30, 20, 40]
arr.remove(20)                     # Removes FIRST 20 only
print(f"remove(20): {arr}")       # [10, 30, 20, 40]

# del — delete by index
arr = [10, 20, 30, 40]
del arr[2]
print(f"del arr[2]: {arr}")       # [10, 20, 40]


# ============================================================
# 2.6 — SLICING (Very Important!)
# ============================================================
"""
Slicing creates a NEW list from a portion of the original.

Syntax: arr[start:end:step]
  - start: starting index (INCLUDED)
  - end:   ending index (EXCLUDED)
  - step:  how many to skip (default 1)

REMEMBER: start is INCLUDED, end is EXCLUDED
"""

print("\n--- Slicing ---")
arr = [10, 20, 30, 40, 50, 60, 70]

print("arr[1:4]  =", arr[1:4])    # [20, 30, 40]  — index 1,2,3 (4 excluded!)
print("arr[:3]   =", arr[:3])     # [10, 20, 30]  — from start to index 2
print("arr[3:]   =", arr[3:])     # [40, 50, 60, 70] — from index 3 to end
print("arr[::2]  =", arr[::2])    # [10, 30, 50, 70] — every 2nd element
print("arr[::-1] =", arr[::-1])   # [70, 60, 50, 40, 30, 20, 10] — REVERSED!
print("arr[-3:]  =", arr[-3:])    # [50, 60, 70] — last 3 elements


# ============================================================
# 2.7 — LOOPING THROUGH A LIST
# ============================================================
"""
There are several ways to loop. Know ALL of them.
"""

print("\n--- Looping ---")
arr = [10, 20, 30]

# Method 1: Simple for loop (when you just need values)
print("Method 1: for loop")
for num in arr:
    print(num, end=" ")  # 10 20 30
print()

# Method 2: Using index (when you need the position)
print("Method 2: using range(len())")
for i in range(len(arr)):
    print(f"arr[{i}] = {arr[i]}")

# Method 3: enumerate (BEST — gives both index AND value)
print("Method 3: enumerate (RECOMMENDED)")
for i, num in enumerate(arr):
    print(f"Index {i}: {num}")

# Method 4: Loop two lists together with zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print("Method 4: zip")
for name, score in zip(names, scores):
    print(f"{name}: {score}")


# ============================================================
# 2.8 — LIST COMPREHENSION (Python Superpower!)
# ============================================================
"""
List comprehension is a SHORT way to create lists.
Syntax: [expression for item in iterable if condition]

This is VERY Pythonic and interviewers love seeing it.
"""

print("\n--- List Comprehension ---")

# Create squares of 1-5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)         # [1, 4, 9, 16, 25]

# Filter: only even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Evens:", evens)             # [2, 4, 6, 8, 10]

# Transform: uppercase
words = ["hello", "world"]
upper = [w.upper() for w in words]
print("Upper:", upper)             # ['HELLO', 'WORLD']

# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)          # [1, 2, 3, 4, 5, 6]


# ============================================================
# 2.9 — SORTING
# ============================================================
"""
sort()    — Sorts IN-PLACE (modifies original list). Returns None.
sorted()  — Returns a NEW sorted list. Original unchanged.
Both use Timsort algorithm: O(n log n)
"""

print("\n--- Sorting ---")
arr = [50, 10, 40, 20, 30]

# sorted() — new list
new_arr = sorted(arr)
print("sorted(arr):", new_arr)     # [10, 20, 30, 40, 50]
print("Original arr:", arr)        # [50, 10, 40, 20, 30] — UNCHANGED

# sort() — in-place
arr.sort()
print("After arr.sort():", arr)    # [10, 20, 30, 40, 50] — MODIFIED

# Reverse sort
arr.sort(reverse=True)
print("Reverse sort:", arr)        # [50, 40, 30, 20, 10]

# Sort by custom key (e.g., sort strings by length)
words = ["banana", "pie", "apple", "hi"]
words.sort(key=len)
print("Sort by length:", words)    # ['hi', 'pie', 'apple', 'banana']

# Sort by custom key (e.g., sort tuples by second element)
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
pairs.sort(key=lambda x: x[1])
print("Sort by second:", pairs)    # [(3, 'a'), (1, 'b'), (2, 'c')]


# ============================================================
# 2.10 — USEFUL BUILT-IN FUNCTIONS
# ============================================================

print("\n--- Useful Built-ins ---")
arr = [3, 1, 4, 1, 5, 9, 2, 6]

print("len(arr):", len(arr))       # 8
print("sum(arr):", sum(arr))       # 31
print("min(arr):", min(arr))       # 1
print("max(arr):", max(arr))       # 9
print("any([0,0,1]):", any([0, 0, 1]))    # True (at least one truthy)
print("all([1,1,1]):", all([1, 1, 1]))    # True (all truthy)
print("all([1,0,1]):", all([1, 0, 1]))    # False

# Check if element exists
print("5 in arr:", 5 in arr)       # True   — O(n) search!
print("99 in arr:", 99 in arr)     # False

# Count occurrences
print("Count of 1:", arr.count(1)) # 2

# Find index of value
print("Index of 5:", arr.index(5)) # 4


# ============================================================
# 2.11 — 2D ARRAYS (MATRIX)
# ============================================================
"""
A 2D array is a "list of lists" — think of it as a table/grid.

    Col:  0   1   2
Row 0: [ 1,  2,  3 ]
Row 1: [ 4,  5,  6 ]
Row 2: [ 7,  8,  9 ]

Access: matrix[row][col]
"""

print("\n--- 2D Arrays ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element at row 0, col 2:", matrix[0][2])  # 3
print("Element at row 2, col 0:", matrix[2][0])  # 7
print("Number of rows:", len(matrix))             # 3
print("Number of cols:", len(matrix[0]))          # 3

# Loop through 2D array
print("\nFull matrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()  # new line after each row

# CAUTION: Creating 2D array (WRONG vs RIGHT way)
# WRONG — all rows point to the SAME list!
wrong = [[0] * 3] * 3
wrong[0][0] = 1
print("\nWrong way:", wrong)   # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] — ALL changed!

# RIGHT — each row is a separate list
right = [[0] * 3 for _ in range(3)]
right[0][0] = 1
print("Right way:", right)    # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] — Only first changed


# ============================================================
# SUMMARY — TIME COMPLEXITY OF LIST OPERATIONS
# ============================================================
"""
Operation               | Time     | Notes
------------------------|----------|------------------
arr[i]                  | O(1)     | Direct access
arr.append(x)           | O(1)*    | Amortized
arr.pop()               | O(1)     | Remove last
arr.pop(i)              | O(n)     | Shifts elements
arr.insert(i, x)        | O(n)     | Shifts elements
arr.remove(x)           | O(n)     | Search + shift
x in arr                | O(n)     | Linear search
arr.sort()              | O(n log n)| Timsort
len(arr)                | O(1)     | Stored internally
arr[a:b]                | O(b-a)   | Creates new list
arr.index(x)            | O(n)     | Linear search
arr.count(x)            | O(n)     | Full scan
min(arr) / max(arr)     | O(n)     | Full scan
sum(arr)                | O(n)     | Full scan
"""


# ============================================================
# QUESTION APPROACH GUIDE — HOW TO SOLVE ARRAY PROBLEMS
# ============================================================
"""
================================================================
STEP-BY-STEP APPROACH FOR ARRAY INTERVIEW QUESTIONS
================================================================

STEP 1: IDENTIFY THE PROBLEM PATTERN
-------------------------------------
Ask yourself these questions:

1. Do I need to find a SUBARRAY (contiguous elements)?
   → Use Sliding Window or Kadane's Algorithm
   Examples: Max sum subarray, longest subarray with condition

2. Do I need to find PAIRS/TRIPLETS with a condition?
   → Use Two Pointers (if sorted) or Hashing (if unsorted)
   Examples: Two sum, three sum, pair with target

3. Do I need to REARRANGE or PARTITION elements?
   → Use Two Pointers (same direction - slow/fast)
   Examples: Move zeros, remove duplicates, Dutch National Flag

4. Do I need to find FREQUENCY or COUNT?
   → Use Hashing (dict/Counter)
   Examples: Most frequent element, find duplicates

5. Is the array SORTED?
   → Consider Binary Search or Two Pointers
   Examples: Search, find range, merge sorted arrays

6. Do I need to track MAXIMUM/MINIMUM over a range?
   → Use Monotonic Stack or Prefix/Suffix arrays
   Examples: Next greater element, trapping rain water


STEP 2: COMMON ARRAY PATTERNS
------------------------------

PATTERN 1: TWO POINTERS (Opposite Direction)
When: Array is sorted, finding pairs, palindrome check
Template:
    left, right = 0, len(arr) - 1
    while left < right:
        if condition_met:
            return result
        elif need_larger_value:
            left += 1
        else:
            right -= 1

PATTERN 2: TWO POINTERS (Same Direction - Slow/Fast)
When: Remove duplicates, move elements, partition
Template:
    slow = 0
    for fast in range(len(arr)):
        if condition(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1
    return slow

PATTERN 3: SLIDING WINDOW (Fixed Size)
When: "Maximum/minimum of subarray size k"
Template:
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

PATTERN 4: SLIDING WINDOW (Variable Size)
When: "Longest/shortest subarray with condition"
Template:
    left = 0
    for right in range(len(arr)):
        add arr[right] to window
        while window violates condition:
            remove arr[left] from window
            left += 1
        update result

PATTERN 5: HASHING
When: Need O(1) lookup, find duplicates, two sum
Template:
    seen = {}  # or set()
    for i, num in enumerate(arr):
        if num in seen:
            return True  # or use seen[num]
        seen[num] = i

PATTERN 6: PREFIX SUM
When: Range sum queries, subarray sum problems
Template:
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    # Sum from i to j: prefix[j+1] - prefix[i]

PATTERN 7: KADANE'S ALGORITHM
When: Maximum sum of contiguous subarray
Template:
    max_sum = current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)


STEP 3: PROBLEM-SOLVING FRAMEWORK
----------------------------------

1. CLARIFY THE PROBLEM
   □ What is the input format?
   □ What is the expected output?
   □ Are there duplicates?
   □ Is the array sorted?
   □ What are the constraints? (size, value range)
   □ What are edge cases? (empty, single element, all same)

2. THINK OF EXAMPLES
   □ Normal case: [1, 2, 3, 4, 5]
   □ Edge case: [], [1], [1, 1, 1]
   □ Negative numbers: [-1, -2, 3]
   □ Large numbers: [1000000, 999999]

3. IDENTIFY THE PATTERN
   □ Match the problem to one of the patterns above
   □ Think about time/space complexity requirements

4. WRITE BRUTE FORCE FIRST (if needed)
   □ Shows you understand the problem
   □ Easier to optimize from working code
   □ Mention: "This is O(n²), we can optimize to O(n)"

5. OPTIMIZE
   □ Can we use a hash map to avoid nested loops?
   □ Can we sort first to enable two pointers?
   □ Can we use sliding window instead of recalculating?

6. CODE CLEANLY
   □ Handle edge cases at the start
   □ Use meaningful variable names
   □ Add comments for complex logic

7. TEST YOUR CODE
   □ Walk through with example
   □ Test edge cases
   □ Check for off-by-one errors


STEP 4: DETAILED PATTERN EXAMPLES
----------------------------------
"""


# --- EXAMPLE 1: Two Sum (Hashing Pattern) ---
def two_sum_approach(nums, target):
    """
    PROBLEM: Find two numbers that add up to target. Return their indices.
    
    APPROACH:
    1. Brute force: O(n²) - check all pairs
    2. Optimized: O(n) - use hash map
    
    WHY HASHING?
    - Need to find if (target - current) exists
    - Hash map gives O(1) lookup
    - Store {value: index} as we iterate
    
    STEP-BY-STEP:
    - For each number, calculate complement = target - number
    - Check if complement is in hash map
    - If yes, return [hash_map[complement], current_index]
    - If no, add current number to hash map
    
    TIME: O(n), SPACE: O(n)
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


# --- EXAMPLE 2: Maximum Subarray (Kadane's Algorithm) ---
def max_subarray_approach(nums):
    """
    PROBLEM: Find the contiguous subarray with the largest sum.
    
    APPROACH:
    1. Brute force: O(n²) - try all subarrays
    2. Optimized: O(n) - Kadane's Algorithm
    
    WHY KADANE'S?
    - At each position, decide: start fresh OR continue current subarray
    - If current_sum + num < num, better to start fresh at num
    - Keep track of global maximum
    
    INTUITION:
    - If adding current element makes sum worse than just the element,
      start a new subarray from current element
    
    STEP-BY-STEP:
    - current_sum = max(num, current_sum + num)
      → Either start fresh or continue
    - max_sum = max(max_sum, current_sum)
      → Track the best we've seen
    
    TIME: O(n), SPACE: O(1)
    """
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# --- EXAMPLE 3: Move Zeros (Two Pointers - Same Direction) ---
def move_zeros_approach(nums):
    """
    PROBLEM: Move all zeros to the end while maintaining order of non-zeros.
    Modify in-place.
    
    APPROACH:
    Use slow/fast pointers
    
    WHY TWO POINTERS?
    - Need to partition: non-zeros on left, zeros on right
    - Slow pointer tracks where to place next non-zero
    - Fast pointer scans through array
    
    STEP-BY-STEP:
    - slow = 0 (position for next non-zero)
    - fast scans from 0 to n-1
    - When fast finds non-zero:
      → Place it at slow position
      → Increment slow
    - After loop, fill remaining positions with zeros
    
    ALTERNATIVE (cleaner):
    - Swap non-zero with position at slow
    - This automatically moves zeros to end
    
    TIME: O(n), SPACE: O(1)
    """
    slow = 0
    
    # Move all non-zeros to the front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    # No need to fill zeros - they're already there from swaps!


# --- EXAMPLE 4: Best Time to Buy/Sell Stock ---
def max_profit_approach(prices):
    """
    PROBLEM: Find max profit from buying and selling stock once.
    Can only buy before you sell.
    
    APPROACH:
    Track minimum price seen so far and maximum profit
    
    WHY THIS WORKS?
    - To maximize profit, buy at lowest price and sell at highest after
    - As we scan, track the minimum price seen so far
    - At each price, calculate profit if we sell today
    - Keep track of maximum profit
    
    STEP-BY-STEP:
    - min_price = infinity (or first price)
    - max_profit = 0
    - For each price:
      → profit = price - min_price
      → max_profit = max(max_profit, profit)
      → min_price = min(min_price, price)
    
    TIME: O(n), SPACE: O(1)
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


# --- EXAMPLE 5: Contains Duplicate (Hashing) ---
def contains_duplicate_approach(nums):
    """
    PROBLEM: Return true if any value appears at least twice.
    
    APPROACH 1: Use a set
    - Add elements to set as we iterate
    - If element already in set, we found a duplicate
    TIME: O(n), SPACE: O(n)
    
    APPROACH 2: Sort first
    - Sort the array
    - Check adjacent elements
    TIME: O(n log n), SPACE: O(1) if in-place sort
    
    APPROACH 3: Compare lengths
    - If len(nums) != len(set(nums)), there are duplicates
    TIME: O(n), SPACE: O(n)
    
    BEST FOR INTERVIEW: Approach 1 (clearest logic)
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False
    
    # One-liner alternative:
    # return len(nums) != len(set(nums))


# --- EXAMPLE 6: Product of Array Except Self ---
def product_except_self_approach(nums):
    """
    PROBLEM: Return array where result[i] = product of all elements except nums[i].
    Cannot use division. Must be O(n).
    
    APPROACH:
    Use prefix and suffix products
    
    WHY THIS WORKS?
    - Product except self = (product of all before) * (product of all after)
    - Build prefix products: prefix[i] = nums[0] * ... * nums[i-1]
    - Build suffix products: suffix[i] = nums[i+1] * ... * nums[n-1]
    - result[i] = prefix[i] * suffix[i]
    
    OPTIMIZATION:
    - Can do in one pass using result array to store prefix
    - Then multiply by suffix in reverse pass
    
    STEP-BY-STEP:
    1. result[i] = product of all elements to the LEFT of i
    2. Traverse right to left, multiply by product of all to the RIGHT
    
    TIME: O(n), SPACE: O(1) excluding output array
    """
    n = len(nums)
    result = [1] * n
    
    # Build prefix products in result
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


"""
================================================================
COMMON MISTAKES TO AVOID
================================================================

❌ Not handling edge cases:
   - Empty array: if not arr: return ...
   - Single element: if len(arr) == 1: return ...
   - All same elements: [5, 5, 5, 5]

❌ Index out of bounds:
   - Always check: if i < len(arr) before accessing arr[i]
   - Be careful with arr[i+1], arr[i-1]

❌ Modifying array while iterating:
   - Use a copy if needed: for num in arr[:]:
   - Or iterate in reverse: for i in range(len(arr)-1, -1, -1):

❌ Using wrong pattern:
   - Don't use sliding window on unsorted array for pair sum
   - Don't use two pointers if array is not sorted (unless same direction)

❌ Forgetting to return:
   - Make sure all code paths return a value

❌ Off-by-one errors:
   - range(n) goes from 0 to n-1
   - arr[a:b] includes a but excludes b
   - Last index is len(arr) - 1

❌ Not considering negative numbers:
   - max_sum might be negative
   - Initialize with arr[0], not 0

❌ Inefficient string concatenation in loops:
   - Use list + join instead of +=


================================================================
INTERVIEW TIPS
================================================================

1. ALWAYS CLARIFY FIRST
   "Can the array be empty?"
   "Are there duplicates?"
   "Is the array sorted?"
   "What's the range of values?"

2. THINK OUT LOUD
   "I'm thinking this is a two-pointer problem because..."
   "We could use hashing here to get O(1) lookup..."
   "The brute force would be O(n²), but we can optimize..."

3. START SIMPLE
   "Let me first write the brute force to make sure I understand..."
   "This works but it's O(n²). Let me optimize it..."

4. TEST AS YOU GO
   "Let me trace through with [1,2,3]..."
   "What if the array is empty?"
   "What if all elements are the same?"

5. STATE COMPLEXITY
   "This solution is O(n) time and O(n) space because..."
   "We can't do better than O(n) because we need to look at every element..."

6. BE READY TO OPTIMIZE
   "We're doing repeated work here - we can cache this..."
   "We're searching multiple times - a hash map would help..."


================================================================
QUICK REFERENCE: WHEN TO USE WHAT
================================================================

SORTED ARRAY:
  → Binary Search: O(log n) search
  → Two Pointers: O(n) for pairs/triplets

UNSORTED ARRAY:
  → Hashing: O(1) lookup, find duplicates, two sum
  → Sorting first: enables two pointers, O(n log n)

SUBARRAY PROBLEMS:
  → Sliding Window: contiguous subarray with condition
  → Prefix Sum: range sum queries
  → Kadane's: maximum sum subarray

PAIR/TRIPLET PROBLEMS:
  → Two Pointers: if sorted
  → Hashing: if unsorted

IN-PLACE MODIFICATION:
  → Two Pointers (slow/fast): remove/move elements
  → Swap elements: partition, Dutch National Flag

FREQUENCY/COUNTING:
  → Hash Map (dict): count occurrences
  → Counter: from collections import Counter


================================================================
PRACTICE STRATEGY
================================================================

1. Master these core problems first:
   □ Two Sum
   □ Best Time to Buy/Sell Stock
   □ Contains Duplicate
   □ Maximum Subarray
   □ Product of Array Except Self
   □ Move Zeros
   □ Three Sum

2. For each problem:
   □ Identify the pattern
   □ Write brute force first
   □ Optimize using the pattern
   □ Test with edge cases
   □ Analyze time/space complexity

3. Build pattern recognition:
   □ See "subarray" → think sliding window
   □ See "pairs" + sorted → think two pointers
   □ See "pairs" + unsorted → think hashing
   □ See "maximum sum" → think Kadane's
   □ See "in-place" → think two pointers

Good luck! 🚀
"""

print("\n✅ Theory complete! Now go to problems_easy.py to practice!")

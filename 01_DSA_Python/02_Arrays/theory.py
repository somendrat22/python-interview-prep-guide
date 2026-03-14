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

print("\n✅ Theory complete! Now go to problems_easy.py to practice!")

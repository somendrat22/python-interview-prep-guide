"""
================================================================
TOPIC 4: HASHING — Dictionaries & Sets (Complete Beginner Guide)
================================================================

================================================================
SECTION 1: WHAT IS HASHING?
================================================================

Hashing is a technique to convert data into a fixed-size value (called a hash)
that acts like an ADDRESS to store/retrieve data instantly.

Think of it like a LIBRARY:
  - Without hashing: You search EVERY shelf to find a book → SLOW (O(n))
  - With hashing: The book's name tells you EXACTLY which shelf → FAST (O(1))

HOW IT WORKS (Simple Explanation):
  1. You have a KEY (e.g., "apple")
  2. A HASH FUNCTION converts the key to a number (e.g., "apple" → 3)
  3. That number is used as an INDEX in an array
  4. Store the value at that index

  Key "apple" → hash("apple") = 3 → store at index 3
  Key "banana" → hash("banana") = 7 → store at index 7
  
  To retrieve: hash("apple") = 3 → go to index 3 → found instantly! O(1)

WHAT IF TWO KEYS MAP TO THE SAME INDEX? (COLLISION)
  e.g., hash("apple") = 3 AND hash("grape") = 3
  This is called a COLLISION.
  Python handles this automatically (using chaining or open addressing).
  You don't need to worry about it, just know it exists.


================================================================
SECTION 2: PYTHON DICTIONARY (dict) — The Hash Map
================================================================

A dictionary stores KEY-VALUE pairs.
  - Keys must be IMMUTABLE (strings, numbers, tuples) and UNIQUE
  - Values can be ANYTHING
  - Lookup by key is O(1) average

Real-world analogy:
  A phone book: Name (key) → Phone Number (value)
  {"Alice": "123-4567", "Bob": "987-6543"}
"""

# ============================================================
# 2.1 — CREATING A DICTIONARY
# ============================================================

# Empty dictionary
empty_dict = {}
print("Empty dict:", empty_dict)        # {}

# Dictionary with values
phone_book = {
    "Alice": "123-4567",
    "Bob": "987-6543",
    "Charlie": "555-1234"
}
print("Phone book:", phone_book)

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print("From tuples:", d)                # {'a': 1, 'b': 2, 'c': 3}

# Using dict comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)              # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 2.2 — ACCESSING VALUES
# ============================================================
"""
Two ways to access:
  d[key]     — Raises KeyError if key doesn't exist
  d.get(key) — Returns None if key doesn't exist (SAFER!)
  d.get(key, default) — Returns default if key doesn't exist
"""

print("\n--- Accessing Values ---")
d = {"apple": 3, "banana": 5, "cherry": 2}

print("d['apple'] =", d["apple"])             # 3
print("d.get('banana') =", d.get("banana"))   # 5
print("d.get('mango') =", d.get("mango"))     # None (no error!)
print("d.get('mango', 0) =", d.get("mango", 0))  # 0 (custom default)

# d['mango']  ← This would CRASH with KeyError!


# ============================================================
# 2.3 — ADDING & MODIFYING
# ============================================================

print("\n--- Adding & Modifying ---")
d = {"apple": 3}

# Add new key-value pair
d["banana"] = 5
print("After adding banana:", d)    # {'apple': 3, 'banana': 5}

# Modify existing value
d["apple"] = 10
print("After modifying apple:", d)  # {'apple': 10, 'banana': 5}


# ============================================================
# 2.4 — REMOVING
# ============================================================
"""
del d[key]    — Remove key. Raises KeyError if not found.
d.pop(key)    — Remove and RETURN value. Raises KeyError if not found.
d.pop(key, default) — Remove and return, or return default if not found.
d.clear()     — Remove ALL items.
"""

print("\n--- Removing ---")
d = {"apple": 3, "banana": 5, "cherry": 2}

# pop — remove and return
val = d.pop("banana")
print(f"Popped banana: {val}, dict: {d}")  # 5, {'apple': 3, 'cherry': 2}

# pop with default — no error if key missing
val = d.pop("mango", -1)
print(f"Popped mango (missing): {val}")    # -1

# del — just remove
del d["cherry"]
print(f"After del cherry: {d}")            # {'apple': 3}


# ============================================================
# 2.5 — CHECKING IF KEY EXISTS
# ============================================================
"""
Use 'in' operator — O(1) average!
This is why dicts are so powerful for interview problems.
"""

print("\n--- Checking Keys ---")
d = {"apple": 3, "banana": 5}

print("'apple' in d:", "apple" in d)     # True
print("'mango' in d:", "mango" in d)     # False

# NEVER do this for checking existence:
# if d["mango"]:  ← CRASHES with KeyError!


# ============================================================
# 2.6 — ITERATING THROUGH A DICTIONARY
# ============================================================

print("\n--- Iterating ---")
d = {"apple": 3, "banana": 5, "cherry": 2}

# Method 1: Iterate over keys (default)
print("Keys:")
for key in d:
    print(f"  {key} → {d[key]}")

# Method 2: Iterate over key-value pairs (RECOMMENDED)
print("Key-Value pairs:")
for key, value in d.items():
    print(f"  {key} → {value}")

# Method 3: Iterate over values only
print("Values only:", list(d.values()))

# Method 4: Iterate over keys only
print("Keys only:", list(d.keys()))


# ============================================================
# 2.7 — USEFUL DICTIONARY METHODS
# ============================================================

print("\n--- Useful Methods ---")
d = {"apple": 3, "banana": 5}

# setdefault — get value, but if key missing, set it first
val = d.setdefault("cherry", 0)  # cherry doesn't exist → add it with value 0
print(f"setdefault('cherry', 0): {val}, dict: {d}")

# update — merge another dict into this one
d.update({"date": 1, "apple": 99})  # apple gets OVERWRITTEN
print(f"After update: {d}")


# ============================================================
# 2.8 — defaultdict (from collections) — Very Useful!
# ============================================================
"""
A defaultdict automatically creates a DEFAULT VALUE for missing keys.
This avoids the need for 'if key in dict' checks.
"""

from collections import defaultdict

print("\n--- defaultdict ---")

# Without defaultdict (verbose):
word_count_normal = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    if word not in word_count_normal:
        word_count_normal[word] = 0
    word_count_normal[word] += 1
print("Normal dict:", word_count_normal)

# With defaultdict (clean!):
word_count_dd = defaultdict(int)  # default value = 0 (int() returns 0)
for word in words:
    word_count_dd[word] += 1      # no need to check if key exists!
print("defaultdict:", dict(word_count_dd))

# defaultdict with list — group items
groups = defaultdict(list)
students = [("A", "Alice"), ("B", "Bob"), ("A", "Amy"), ("B", "Ben")]
for grade, name in students:
    groups[grade].append(name)
print("Groups:", dict(groups))  # {'A': ['Alice', 'Amy'], 'B': ['Bob', 'Ben']}


# ============================================================
# 2.9 — Counter (from collections) — Frequency Counting
# ============================================================
"""
Counter is a specialized dict for counting things.
EXTREMELY useful in interviews!
"""

from collections import Counter

print("\n--- Counter ---")

# Count characters in a string
freq = Counter("abracadabra")
print("Character freq:", freq)          # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Count elements in a list
nums = [1, 2, 3, 2, 1, 3, 3, 4]
freq = Counter(nums)
print("Number freq:", freq)             # Counter({3: 3, 1: 2, 2: 2, 4: 1})

# Most common elements
print("Most common 2:", freq.most_common(2))  # [(3, 3), (1, 2)]

# Access count of specific element
print("Count of 3:", freq[3])           # 3
print("Count of 99:", freq[99])         # 0 (no KeyError!)


# ============================================================
# SECTION 3: PYTHON SET — The Hash Set
# ============================================================
"""
A set is a collection of UNIQUE elements with NO ORDER.
  - No duplicates allowed
  - Lookup is O(1) average (uses hashing internally)
  - Cannot access by index (no ordering!)

When to use SET vs LIST:
  - Need fast lookup? → SET (O(1) vs O(n))
  - Need ordering/indexing? → LIST
  - Need uniqueness? → SET
"""

print("\n" + "=" * 60)
print("SETS")
print("=" * 60)

# ============================================================
# 3.1 — CREATING A SET
# ============================================================

# From a list (automatically removes duplicates!)
s = set([1, 2, 3, 2, 1])
print("Set from list:", s)             # {1, 2, 3}

# Direct creation
s = {1, 2, 3, 4, 5}
print("Direct set:", s)

# Empty set — MUST use set(), NOT {}
empty_set = set()     # correct!
empty_dict = {}       # this creates an EMPTY DICT, not a set!
print(f"Type of set(): {type(empty_set)}")    # <class 'set'>
print(f"Type of {{}}: {type(empty_dict)}")     # <class 'dict'>

# Set from string
char_set = set("hello")
print("Set from 'hello':", char_set)  # {'h', 'e', 'l', 'o'} — no duplicate 'l'!


# ============================================================
# 3.2 — SET OPERATIONS
# ============================================================

print("\n--- Set Operations ---")
s = {1, 2, 3}

# Add element
s.add(4)
print("After add(4):", s)             # {1, 2, 3, 4}
s.add(3)                               # 3 already exists — no effect
print("After add(3):", s)             # {1, 2, 3, 4}

# Remove element
s.remove(2)                            # Raises KeyError if not found
print("After remove(2):", s)          # {1, 3, 4}

s.discard(99)                          # Does NOT raise error if not found
print("After discard(99):", s)        # {1, 3, 4}

# Check membership — O(1)!
print("3 in s:", 3 in s)              # True
print("99 in s:", 99 in s)            # False


# ============================================================
# 3.3 — SET MATH OPERATIONS
# ============================================================
"""
These are very useful in interviews!

    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    
    Union (A | B):        {1, 2, 3, 4, 5, 6}  — everything from both
    Intersection (A & B): {3, 4}               — common elements
    Difference (A - B):   {1, 2}               — in A but not in B
    Symmetric Diff (A ^ B): {1, 2, 5, 6}      — in one but not both
"""

print("\n--- Set Math ---")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A | B (union):        {A | B}")        # {1, 2, 3, 4, 5, 6}
print(f"A & B (intersection): {A & B}")        # {3, 4}
print(f"A - B (difference):   {A - B}")        # {1, 2}
print(f"A ^ B (symmetric):    {A ^ B}")        # {1, 2, 5, 6}
print(f"A.issubset(B):        {A.issubset(B)}") # False
print(f"{{3,4}}.issubset(A):    {{3,4}}.issubset(A) = {({3,4}).issubset(A)}")  # True


# ============================================================
# SUMMARY — TIME COMPLEXITIES
# ============================================================
"""
DICTIONARY:
Operation          | Average | Worst
-------------------|---------|------
d[key]             | O(1)    | O(n)
d[key] = val       | O(1)    | O(n)
key in d           | O(1)    | O(n)
del d[key]         | O(1)    | O(n)
d.keys()/values()  | O(1)    | O(1)  (returns view)
for k in d         | O(n)    | O(n)
len(d)             | O(1)    | O(1)

SET:
Operation          | Average | Worst
-------------------|---------|------
s.add(x)           | O(1)    | O(n)
x in s             | O(1)    | O(n)
s.remove(x)        | O(1)    | O(n)
s | t (union)      | O(len(s)+len(t))
s & t (intersect)  | O(min(len(s),len(t)))
s - t (diff)       | O(len(s))

Note: Worst case O(n) happens due to hash collisions.
      In practice, it's almost always O(1).

WHEN TO USE WHAT:
  - Need key-value pairs?     → dict
  - Need just unique values?  → set  
  - Need fast lookup?         → dict or set (both O(1))
  - Need to count things?     → Counter (from collections)
  - Need to group things?     → defaultdict(list)
"""

print("\n✅ Hashing theory complete! Now go to problems_easy.py!")

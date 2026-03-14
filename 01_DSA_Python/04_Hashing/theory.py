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


# ============================================================
# QUESTION APPROACH GUIDE — HOW TO SOLVE HASHING PROBLEMS
# ============================================================
"""
================================================================
HASHING PROBLEM PATTERNS & APPROACHES
================================================================

PATTERN 1: FREQUENCY COUNTING
------------------------------
When: "Count occurrences", "most frequent", "find duplicates"

Approach: Hash Map (dict) or Counter

Template:
```python
from collections import Counter

def frequency_pattern(arr):
    # Method 1: Counter (cleanest)
    freq = Counter(arr)
    
    # Method 2: Manual dict
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    
    # Method 3: defaultdict
    from collections import defaultdict
    freq = defaultdict(int)
    for item in arr:
        freq[item] += 1
    
    return freq
```

Example Problems:
- Majority Element (appears > n/2 times)
- Top K Frequent Elements
- First Unique Character
- Contains Duplicate


PATTERN 2: TWO SUM VARIANTS
----------------------------
When: "Find two elements that sum to target"

Approach: Hash Map for O(1) lookup

Template:
```python
def two_sum(nums, target):
    seen = {}  # {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []
```

Variants:
- Two Sum: return indices
- Two Sum II: sorted array (use two pointers instead!)
- Two Sum III: design data structure
- 3Sum: fix one element, two sum on rest
- 4Sum: fix two elements, two sum on rest

Example Problems:
- Two Sum (LeetCode 1)
- 3Sum (LeetCode 15)
- 4Sum (LeetCode 18)


PATTERN 3: GROUPING/CATEGORIZING
---------------------------------
When: "Group items by property", "categorize elements"

Approach: Hash Map with lists as values

Template:
```python
from collections import defaultdict

def group_pattern(items):
    groups = defaultdict(list)
    
    for item in items:
        key = get_key(item)  # Define how to categorize
        groups[key].append(item)
    
    return list(groups.values())
```

Example Problems:
- Group Anagrams (key = sorted string)
- Group Shifted Strings
- Partition Labels


PATTERN 4: SUBARRAY SUM PROBLEMS
---------------------------------
When: "Subarray sum equals k", "continuous subarray sum"

Approach: Prefix Sum + Hash Map

Template:
```python
def subarray_sum_equals_k(nums, k):
    # Key insight: if prefix_sum[j] - prefix_sum[i] = k,
    # then subarray from i+1 to j has sum k
    
    prefix_sum = 0
    sum_count = {0: 1}  # {prefix_sum: count}
    count = 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Add current prefix_sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

Key Insight:
- prefix_sum[j] - prefix_sum[i] = sum of subarray from i+1 to j
- If we want sum = k, we need prefix_sum[j] - k = prefix_sum[i]
- So check if (current_prefix_sum - k) exists in hash map

Example Problems:
- Subarray Sum Equals K (LeetCode 560)
- Continuous Subarray Sum (LeetCode 523)
- Contiguous Array (LeetCode 525)


PATTERN 5: CHECKING EXISTENCE
------------------------------
When: "Does element exist?", "find missing number"

Approach: Hash Set for O(1) lookup

Template:
```python
def existence_pattern(arr):
    seen = set(arr)
    
    # Check if element exists
    if target in seen:
        return True
    
    # Find missing element
    for i in range(expected_range):
        if i not in seen:
            return i
```

Example Problems:
- Contains Duplicate
- Missing Number
- First Missing Positive
- Longest Consecutive Sequence


PATTERN 6: MAPPING/TRANSLATION
-------------------------------
When: "Map one thing to another", "isomorphic", "word pattern"

Approach: Two Hash Maps (bidirectional mapping)

Template:
```python
def isomorphic_pattern(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for c1, c2 in zip(s, t):
        # Check if mapping exists and is consistent
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2
        
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
    
    return True
```

Example Problems:
- Isomorphic Strings (LeetCode 205)
- Word Pattern (LeetCode 290)
- Valid Anagram


================================================================
DETAILED EXAMPLE SOLUTIONS
================================================================
"""


# --- EXAMPLE 1: Two Sum ---
def two_sum_detailed(nums, target):
    """
    PROBLEM: Find two numbers that add up to target. Return indices.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (because nums[0] + nums[1] = 9)
    
    APPROACH: Hash Map
    
    WHY HASHING?
    - Brute force: O(n²) - check all pairs
    - With hash map: O(n) - single pass
    - For each number, check if (target - number) exists
    
    STEP-BY-STEP:
    1. Create hash map to store {value: index}
    2. For each number:
       - Calculate complement = target - number
       - If complement in hash map, found the pair!
       - Otherwise, add current number to hash map
    
    WHY THIS WORKS:
    - When we see number x, we check if (target - x) was seen before
    - If yes, we found the pair
    - If no, we save x for future numbers to find
    
    TIME: O(n), SPACE: O(n)
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []


# --- EXAMPLE 2: Group Anagrams ---
def group_anagrams_detailed(strs):
    """
    PROBLEM: Group anagrams together.
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    APPROACH: Hash Map with Sorted String as Key
    
    WHY THIS WORKS?
    - Anagrams have same characters, different order
    - When sorted, anagrams become identical: "eat" → "aet", "tea" → "aet"
    - Use sorted string as key to group
    
    STEP-BY-STEP:
    1. Create hash map: {sorted_string: [original_strings]}
    2. For each string:
       - Sort it to get the key
       - Add original string to list at that key
    3. Return all values (groups)
    
    OPTIMIZATION:
    - Instead of sorting (O(k log k)), use character count tuple as key (O(k))
    - count = [0]*26 for each letter, convert to tuple
    
    TIME: O(n * k log k) where n = number of strings, k = max length
    SPACE: O(n * k)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Sort string to get key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


# --- EXAMPLE 3: Subarray Sum Equals K ---
def subarray_sum_k_detailed(nums, k):
    """
    PROBLEM: Count subarrays with sum equal to k.
    Input: nums = [1,1,1], k = 2
    Output: 2 (subarrays [1,1] appear twice)
    
    APPROACH: Prefix Sum + Hash Map
    
    KEY INSIGHT:
    - prefix_sum[j] = sum from 0 to j
    - Sum from i to j = prefix_sum[j] - prefix_sum[i-1]
    - If we want sum = k, then: prefix_sum[j] - prefix_sum[i-1] = k
    - Rearrange: prefix_sum[i-1] = prefix_sum[j] - k
    - So check if (current_prefix_sum - k) exists!
    
    STEP-BY-STEP:
    1. Keep running prefix sum
    2. Hash map stores {prefix_sum: count of times seen}
    3. For each element:
       - Add to prefix_sum
       - Check if (prefix_sum - k) exists in map
       - If yes, add its count to result (those are valid subarrays)
       - Add current prefix_sum to map
    
    EDGE CASE:
    - Initialize map with {0: 1} to handle subarrays starting from index 0
    
    TIME: O(n), SPACE: O(n)
    """
    prefix_sum = 0
    sum_count = {0: 1}  # {prefix_sum: count}
    count = 0
    
    for num in nums:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, we found subarrays
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Add current prefix_sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


# --- EXAMPLE 4: Longest Consecutive Sequence ---
def longest_consecutive_detailed(nums):
    """
    PROBLEM: Find length of longest consecutive sequence.
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4 (sequence [1, 2, 3, 4])
    
    APPROACH: Hash Set
    
    WHY HASH SET?
    - Need O(1) lookup to check if number exists
    - Don't care about order or duplicates
    
    KEY INSIGHT:
    - Only start counting from the START of a sequence
    - How to know if it's the start? Check if (num - 1) exists
    - If (num - 1) doesn't exist, num is the start!
    
    STEP-BY-STEP:
    1. Put all numbers in a set
    2. For each number:
       - Check if it's the start of a sequence (num-1 not in set)
       - If yes, count consecutive numbers: num, num+1, num+2, ...
       - Track maximum length
    
    WHY O(n)?
    - Each number is visited at most twice:
      - Once in outer loop
      - Once in inner loop (only if it's part of a sequence)
    
    TIME: O(n), SPACE: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if this is the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


# --- EXAMPLE 5: Top K Frequent Elements ---
def top_k_frequent_detailed(nums, k):
    """
    PROBLEM: Return k most frequent elements.
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
    APPROACH 1: Counter + Sorting
    - Count frequencies
    - Sort by frequency
    - Return top k
    TIME: O(n log n)
    
    APPROACH 2: Counter + Heap
    - Count frequencies
    - Use min heap of size k
    - Return heap contents
    TIME: O(n log k)
    
    APPROACH 3: Bucket Sort (Optimal)
    - Count frequencies
    - Create buckets: bucket[freq] = [elements with that frequency]
    - Iterate from highest frequency to get top k
    TIME: O(n)
    """
    from collections import Counter
    
    # Method 1: Counter + most_common (uses heap internally)
    freq = Counter(nums)
    return [num for num, count in freq.most_common(k)]
    
    # Method 2: Bucket sort (O(n))
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Put elements in buckets by frequency
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Collect top k from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result


# --- EXAMPLE 6: First Missing Positive ---
def first_missing_positive_detailed(nums):
    """
    PROBLEM: Find smallest missing positive integer.
    Input: [3,4,-1,1] → Output: 2
    Input: [7,8,9,11,12] → Output: 1
    
    APPROACH: Use Array as Hash Map (In-Place)
    
    KEY INSIGHT:
    - Answer must be in range [1, n+1] where n = len(nums)
    - Why? If all numbers 1 to n are present, answer is n+1
    - Use array indices as hash map: index i represents number i+1
    
    STEP-BY-STEP:
    1. Mark presence by making values negative
    2. For each number x in range [1, n]:
       - Mark index (x-1) as negative
    3. First positive index i means (i+1) is missing
    
    HANDLING EDGE CASES:
    - Ignore numbers <= 0 and > n
    - Handle duplicates
    
    TIME: O(n), SPACE: O(1)
    """
    n = len(nums)
    
    # Step 1: Replace non-positive and > n with n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark presence by making index negative
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find first positive index
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1


"""
================================================================
COMMON HASHING MISTAKES
================================================================

❌ Using list for membership check:
   if x in my_list:  # O(n) - SLOW!
   
   ✓ Use set:
   if x in my_set:  # O(1) - FAST!

❌ Not handling hash collisions (Python does this automatically):
   - You don't need to worry about this in Python
   - dict and set handle collisions internally

❌ Using mutable objects as dict keys:
   my_dict[list] = value  # ERROR! Lists are mutable
   
   ✓ Use immutable types:
   my_dict[tuple] = value  # OK! Tuples are immutable

❌ Forgetting defaultdict vs regular dict:
   freq = {}
   freq[key] += 1  # KeyError if key doesn't exist!
   
   ✓ Use get() or defaultdict:
   freq[key] = freq.get(key, 0) + 1
   # OR
   from collections import defaultdict
   freq = defaultdict(int)
   freq[key] += 1

❌ Not considering space complexity:
   - Hash maps use O(n) extra space
   - Sometimes interviewer wants O(1) space solution


================================================================
INTERVIEW TIPS FOR HASHING PROBLEMS
================================================================

1. RECOGNIZE WHEN TO USE HASHING
   - "Find duplicates" → Set
   - "Count frequency" → Counter/dict
   - "Two sum" → Hash map
   - "Group by property" → Hash map with lists
   - "Check existence in O(1)" → Set

2. CHOOSE RIGHT DATA STRUCTURE
   - Need just existence? → set
   - Need value mapping? → dict
   - Need frequency? → Counter
   - Need default values? → defaultdict

3. THINK ABOUT TRADE-OFFS
   - Hash map: O(1) lookup but O(n) space
   - Sorting: O(n log n) time but O(1) space (in-place)
   - Two pointers: O(n) time and O(1) space (if sorted)

4. COMMON PATTERNS TO MENTION
   - "We can use a hash map to get O(1) lookup..."
   - "This avoids the O(n²) nested loop..."
   - "Counter makes frequency counting clean..."

5. TEST EDGE CASES
   - Empty input
   - Single element
   - All duplicates
   - No duplicates


================================================================
QUICK REFERENCE
================================================================

FREQUENCY COUNTING:
  → Counter(arr) or manual dict

TWO SUM:
  → seen = {}; check if (target - num) in seen

GROUPING:
  → defaultdict(list); groups[key].append(item)

SUBARRAY SUM:
  → Prefix sum + hash map of {prefix_sum: count}

EXISTENCE CHECK:
  → Use set for O(1) lookup

ANAGRAMS:
  → Use sorted string or char frequency as key

Good luck! 🚀
"""

print("\n✅ Hashing theory complete! Now go to problems_easy.py!")

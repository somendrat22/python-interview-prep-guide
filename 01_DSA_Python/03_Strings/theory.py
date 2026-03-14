"""
================================================================
TOPIC 3: STRINGS — Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A STRING?
================================================================

A string is a SEQUENCE of characters. Each character has a position (index),
just like an array.

    Index:   0   1   2   3   4
           +---+---+---+---+---+
    Value: | H | e | l | l | o |
           +---+---+---+---+---+
    
    s = "Hello"
    s[0] = 'H'
    s[4] = 'o'
    s[-1] = 'o'  (last character)

KEY DIFFERENCE FROM ARRAYS:
  - Strings are IMMUTABLE in Python
  - You CANNOT change a character in a string:
      s = "Hello"
      s[0] = 'h'  ← THIS WILL GIVE AN ERROR!
  - To "modify" a string, you must create a NEW string


================================================================
SECTION 2: WHY ARE STRINGS IMPORTANT?
================================================================
  - Strings are asked in EVERY coding interview
  - Many array techniques also apply to strings
  - String problems test your knowledge of:
    → Character manipulation
    → Pattern matching
    → Hashing/frequency counting
    → Two pointers


================================================================
SECTION 3: CREATING STRINGS
================================================================
"""

# Single quotes or double quotes — both work the same
s1 = 'Hello'
s2 = "Hello"
print(s1 == s2)   # True — they are identical

# Multi-line string
s3 = """This is
a multi-line
string"""
print(s3)

# Empty string
empty = ""
print(f"Empty string length: {len(empty)}")  # 0

# String from number
num_str = str(42)       # "42"
print(f"Number to string: {num_str}, type: {type(num_str)}")

# String to number
back_to_num = int("42")  # 42
print(f"String to number: {back_to_num}, type: {type(back_to_num)}")


# ============================================================
# SECTION 4: ACCESSING CHARACTERS
# ============================================================
"""
Just like arrays, use index. Strings support:
  - Positive indexing (left to right): 0, 1, 2, ...
  - Negative indexing (right to left): -1, -2, -3, ...
  - Slicing: s[start:end:step]
"""

print("\n--- Accessing Characters ---")
s = "Python"

print(f"s[0] = '{s[0]}'")      # 'P'
print(f"s[2] = '{s[2]}'")      # 't'
print(f"s[-1] = '{s[-1]}'")    # 'n'
print(f"s[-2] = '{s[-2]}'")    # 'o'
print(f"len(s) = {len(s)}")    # 6

# Slicing
print(f"s[0:3] = '{s[0:3]}'")  # 'Pyt' (index 0,1,2 — 3 excluded!)
print(f"s[2:] = '{s[2:]}'")    # 'thon' (from index 2 to end)
print(f"s[:3] = '{s[:3]}'")    # 'Pyt' (from start to index 2)
print(f"s[::-1] = '{s[::-1]}'")# 'nohtyP' (REVERSED!)

# Iterate through characters
print("\nIterating:")
for i, ch in enumerate(s):
    print(f"  s[{i}] = '{ch}'")


# ============================================================
# SECTION 5: STRING METHODS (Must Know!)
# ============================================================
"""
Strings have MANY built-in methods. These are the important ones:
"""

print("\n--- String Methods ---")
s = "  Hello, World!  "

# --- Changing Case ---
print("'hello'.upper()   =", "hello".upper())     # 'HELLO'
print("'HELLO'.lower()   =", "HELLO".lower())     # 'hello'
print("'hello'.capitalize() =", "hello".capitalize())  # 'Hello'
print("'hello world'.title() =", "hello world".title())  # 'Hello World'
print("'Hello'.swapcase() =", "Hello".swapcase())  # 'hELLO'

# --- Stripping Whitespace ---
print(f"\n'{s}'.strip()  = '{s.strip()}'")     # 'Hello, World!'
print(f"'{s}'.lstrip() = '{s.lstrip()}'")      # 'Hello, World!  '
print(f"'{s}'.rstrip() = '{s.rstrip()}'")      # '  Hello, World!'

# --- Searching ---
s = "Hello, World!"
print(f"\n'World' in s = {'World' in s}")       # True  (O(n) — use this for checking!)
print(f"s.find('World') = {s.find('World')}")   # 7   (returns index, -1 if not found)
print(f"s.find('xyz')   = {s.find('xyz')}")     # -1
print(f"s.index('World') = {s.index('World')}") # 7   (like find, but RAISES ERROR if not found)
print(f"s.count('l')    = {s.count('l')}")      # 3
print(f"s.startswith('Hello') = {s.startswith('Hello')}")  # True
print(f"s.endswith('!')       = {s.endswith('!')}")        # True

# --- Splitting and Joining ---
s = "apple,banana,cherry"
parts = s.split(",")                # Split by comma
print(f"\n'{s}'.split(',') = {parts}")   # ['apple', 'banana', 'cherry']

joined = " - ".join(parts)          # Join with ' - '
print(f"' - '.join(parts) = '{joined}'")  # 'apple - banana - cherry'

words = "Hello World Python".split()  # Split by whitespace (default)
print(f"Split by space: {words}")      # ['Hello', 'World', 'Python']

# --- Replacing ---
s = "Hello World"
print(f"\n'{s}'.replace('World', 'Python') = '{s.replace('World', 'Python')}'")
# 'Hello Python'

# --- Checking Character Types ---
print("\n--- Character Checks ---")
print("'abc'.isalpha()  =", "abc".isalpha())     # True (all letters)
print("'123'.isdigit()  =", "123".isdigit())     # True (all digits)
print("'abc123'.isalnum()=", "abc123".isalnum())  # True (letters or digits)
print("'   '.isspace()  =", "   ".isspace())     # True (all whitespace)


# ============================================================
# SECTION 6: STRING IMMUTABILITY — Very Important!
# ============================================================
"""
STRINGS CANNOT BE MODIFIED. Every operation creates a NEW string.

This has a BIG impact on performance:
"""

print("\n--- Immutability ---")
s = "Hello"

# You CANNOT do this:
# s[0] = 'h'  ← TypeError!

# Instead, create a new string:
s_new = 'h' + s[1:]
print(f"Changed first char: '{s_new}'")  # 'hello'

# PERFORMANCE WARNING: String concatenation in a loop
# BAD — O(n²) because each + creates a new string
def build_string_bad(n):
    result = ""
    for i in range(n):
        result += str(i)  # Each += copies the ENTIRE string + adds new char
    return result

# GOOD — O(n) using list + join
def build_string_good(n):
    parts = []
    for i in range(n):
        parts.append(str(i))  # O(1) append
    return "".join(parts)      # O(n) join at the end

# BEST — O(n) using list comprehension
def build_string_best(n):
    return "".join(str(i) for i in range(n))


# ============================================================
# SECTION 7: CONVERTING BETWEEN STRINGS AND LISTS
# ============================================================
"""
Since strings are immutable, a common pattern is:
  1. Convert string to list of characters
  2. Modify the list
  3. Convert back to string
"""

print("\n--- String ↔ List Conversion ---")

# String to list of characters
s = "Hello"
char_list = list(s)
print(f"list('{s}') = {char_list}")  # ['H', 'e', 'l', 'l', 'o']

# Modify the list
char_list[0] = 'h'
print(f"After modification: {char_list}")  # ['h', 'e', 'l', 'l', 'o']

# List back to string
s_new = "".join(char_list)
print(f"''.join(char_list) = '{s_new}'")  # 'hello'


# ============================================================
# SECTION 8: ASCII VALUES
# ============================================================
"""
Every character has a number (ASCII value).
This is useful for many string problems.

Important ASCII values:
  'a' = 97,  'z' = 122  (26 lowercase letters)
  'A' = 65,  'Z' = 90   (26 uppercase letters)
  '0' = 48,  '9' = 57   (10 digits)

Functions:
  ord('a') → 97    (character to number)
  chr(97)  → 'a'   (number to character)
"""

print("\n--- ASCII Values ---")
print(f"ord('a') = {ord('a')}")    # 97
print(f"ord('z') = {ord('z')}")    # 122
print(f"ord('A') = {ord('A')}")    # 65
print(f"ord('0') = {ord('0')}")    # 48
print(f"chr(97)  = '{chr(97)}'")   # 'a'
print(f"chr(65)  = '{chr(65)}'")   # 'A'

# Useful trick: position in alphabet
ch = 'd'
position = ord(ch) - ord('a')  # 'd' - 'a' = 100 - 97 = 3 (0-indexed)
print(f"'{ch}' is at position {position} in alphabet (0-indexed)")

# Useful trick: is it a lowercase letter?
def is_lowercase(ch):
    return ord('a') <= ord(ch) <= ord('z')

# Useful trick: convert lowercase to uppercase manually
def to_upper_manual(ch):
    if is_lowercase(ch):
        return chr(ord(ch) - 32)  # difference between 'a'(97) and 'A'(65) is 32
    return ch

print(f"Manual uppercase of 'h': '{to_upper_manual('h')}'")  # 'H'


# ============================================================
# SECTION 9: COMMON STRING PATTERNS
# ============================================================
"""
These patterns come up again and again in interviews:

1. Frequency Count — count occurrences of each character
2. Two Pointers — check palindrome, compare from both ends
3. Sliding Window — find substrings with certain properties
4. String Building — build result character by character
"""

# Pattern: Frequency Count
from collections import Counter

s = "abracadabra"
freq = Counter(s)
print(f"\nFrequency of '{s}': {dict(freq)}")
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Manual frequency count (without Counter)
freq_manual = {}
for ch in s:
    freq_manual[ch] = freq_manual.get(ch, 0) + 1
print(f"Manual frequency: {freq_manual}")


# ============================================================
# SUMMARY OF TIME COMPLEXITIES
# ============================================================
"""
Operation                    | Time     | Notes
-----------------------------|----------|------------------
s[i]                        | O(1)     | Index access
len(s)                      | O(1)     | Stored internally
s + t                       | O(n+m)   | Creates new string
s * k                       | O(n*k)   | Repeats string
x in s                      | O(n)     | Substring search
s.find(x)                   | O(n*m)   | Worst case
s.split()                   | O(n)     |
"".join(list)               | O(n)     | Total chars
s.replace(old, new)         | O(n)     |
s.strip()                   | O(n)     |
s.lower() / s.upper()       | O(n)     |
s[::-1]                     | O(n)     | Reverse
s == t                      | O(n)     | Compare char by char
"""


# ============================================================
# QUESTION APPROACH GUIDE — HOW TO SOLVE STRING PROBLEMS
# ============================================================
"""
================================================================
STRING PROBLEM PATTERNS & APPROACHES
================================================================

PATTERN 1: PALINDROME PROBLEMS
-------------------------------
When: "Check if palindrome", "longest palindrome", "valid palindrome"

Approach: Two Pointers (opposite direction)

Template:
```python
def is_palindrome(s):
    # Clean string: remove non-alphanumeric, convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Key Points:
- Clean the string first (remove spaces, punctuation, lowercase)
- Compare from both ends moving inward
- Can also reverse and compare: s == s[::-1]

Example Problems:
- Valid Palindrome (LeetCode 125)
- Valid Palindrome II (can delete one char)
- Longest Palindromic Substring


PATTERN 2: ANAGRAM PROBLEMS
----------------------------
When: "Check if anagram", "group anagrams", "find anagrams"

Approach: Frequency Counting (Hash Map or Counter)

Template:
```python
from collections import Counter

def is_anagram(s, t):
    # Method 1: Counter
    return Counter(s) == Counter(t)
    
    # Method 2: Sorted
    return sorted(s) == sorted(t)
    
    # Method 3: Manual frequency
    if len(s) != len(t):
        return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        freq[c] = freq.get(c, 0) - 1
        if freq[c] < 0:
            return False
    return True
```

Key Points:
- Anagrams have same character frequency
- Counter is cleanest for interviews
- sorted() works but O(n log n)

Example Problems:
- Valid Anagram (LeetCode 242)
- Group Anagrams (LeetCode 49)
- Find All Anagrams in String (LeetCode 438)


PATTERN 3: SUBSTRING WITH CONDITION (Sliding Window)
-----------------------------------------------------
When: "Longest substring without repeating", "minimum window", "substring with k distinct"

Approach: Sliding Window with Hash Map/Set

Template (Variable Size):
```python
def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Shrink window while condition violated
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

Template (With Frequency Map):
```python
def min_window_substring(s, t):
    from collections import Counter
    
    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    
    left = 0
    min_len = float('inf')
    result = ""
    
    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1
        
        if char in need and have[char] == need[char]:
            formed += 1
        
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]
            
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    
    return result
```

Key Points:
- Use set for unique characters
- Use dict/Counter for frequency
- Expand right, shrink left when condition met

Example Problems:
- Longest Substring Without Repeating Characters (LeetCode 3)
- Minimum Window Substring (LeetCode 76)
- Longest Substring with At Most K Distinct Characters


PATTERN 4: STRING MANIPULATION (Build Result)
----------------------------------------------
When: "Reverse words", "compress string", "remove characters"

Approach: Convert to list, modify, join back

Template:
```python
def reverse_words(s):
    # Split, reverse, join
    words = s.split()
    return ' '.join(reversed(words))
    
    # Or manually
    words = s.split()
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return ' '.join(words)
```

Key Points:
- Strings are immutable - use list for modifications
- Use ''.join() to build final string (O(n))
- Avoid += in loops (O(n²))

Example Problems:
- Reverse Words in String (LeetCode 151)
- String Compression (LeetCode 443)
- Remove Duplicates from String


PATTERN 5: PARENTHESES/BRACKETS (Stack)
----------------------------------------
When: "Valid parentheses", "remove invalid", "decode string"

Approach: Stack

Template:
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0
```

Key Points:
- Stack for matching pairs
- Map closing to opening brackets
- Stack should be empty at end

Example Problems:
- Valid Parentheses (LeetCode 20)
- Remove Invalid Parentheses (LeetCode 301)
- Decode String (LeetCode 394)


PATTERN 6: TWO STRING COMPARISON
---------------------------------
When: "Is subsequence", "edit distance", "longest common prefix"

Approach: Two Pointers or Dynamic Programming

Template (Subsequence):
```python
def is_subsequence(s, t):
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)
```

Template (Longest Common Prefix):
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]
```

Example Problems:
- Is Subsequence (LeetCode 392)
- Longest Common Prefix (LeetCode 14)
- Edit Distance (LeetCode 72) - DP


PATTERN 7: CHARACTER MANIPULATION
----------------------------------
When: Working with ASCII values, character types, case conversion

Template:
```python
# Check character type
c.isalpha()   # letter
c.isdigit()   # digit
c.isalnum()   # letter or digit
c.isspace()   # whitespace
c.isupper()   # uppercase
c.islower()   # lowercase

# Convert case
c.upper()
c.lower()

# ASCII values
ord('a')  # 97
chr(97)   # 'a'

# Position in alphabet (0-indexed)
pos = ord(c.lower()) - ord('a')  # 0-25

# Shift character (Caesar cipher)
shifted = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
```

Example Problems:
- Caesar Cipher
- Reverse Only Letters
- Detect Capital


================================================================
DETAILED EXAMPLE SOLUTIONS
================================================================
"""


# --- EXAMPLE 1: Longest Substring Without Repeating Characters ---
def longest_substring_no_repeat(s):
    """
    PROBLEM: Find length of longest substring without repeating characters.
    Input: "abcabcbb" → Output: 3 ("abc")
    
    APPROACH: Sliding Window with Set
    
    WHY SLIDING WINDOW?
    - Need contiguous substring
    - Condition: no repeating characters
    - Expand window, shrink when duplicate found
    
    STEP-BY-STEP:
    1. Use set to track characters in current window
    2. Expand right pointer, add character to set
    3. If duplicate found, shrink from left until duplicate removed
    4. Track maximum window size
    
    TIME: O(n), SPACE: O(min(n, 26)) for lowercase letters
    """
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Shrink window while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len


# --- EXAMPLE 2: Group Anagrams ---
def group_anagrams_approach(strs):
    """
    PROBLEM: Group strings that are anagrams of each other.
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    APPROACH: Hash Map with Sorted String as Key
    
    WHY THIS WORKS?
    - Anagrams have same characters, just different order
    - When sorted, anagrams become identical
    - Use sorted string as key to group anagrams
    
    ALTERNATIVE: Use character frequency tuple as key
    
    STEP-BY-STEP:
    1. Create hash map: {sorted_string: [original_strings]}
    2. For each string, sort it to get key
    3. Add original string to list at that key
    4. Return all values from hash map
    
    TIME: O(n * k log k) where n=number of strings, k=max length
    SPACE: O(n * k)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
    
    # Alternative: Use frequency tuple as key (faster)
    # groups = defaultdict(list)
    # for s in strs:
    #     count = [0] * 26
    #     for c in s:
    #         count[ord(c) - ord('a')] += 1
    #     groups[tuple(count)].append(s)
    # return list(groups.values())


# --- EXAMPLE 3: Valid Palindrome ---
def valid_palindrome_approach(s):
    """
    PROBLEM: Check if string is palindrome (ignore non-alphanumeric, case-insensitive).
    Input: "A man, a plan, a canal: Panama" → Output: True
    
    APPROACH: Two Pointers after cleaning
    
    STEP-BY-STEP:
    1. Clean string: keep only alphanumeric, convert to lowercase
    2. Use two pointers from both ends
    3. Compare characters, move pointers inward
    4. If all match, it's a palindrome
    
    ALTERNATIVE: Clean and compare with reverse
    
    TIME: O(n), SPACE: O(n) for cleaned string
    """
    # Method 1: Clean then compare
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
    
    # Method 2: Two pointers (more space efficient)
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# --- EXAMPLE 4: Reverse Words in String ---
def reverse_words_approach(s):
    """
    PROBLEM: Reverse order of words in string.
    Input: "  hello world  " → Output: "world hello"
    
    APPROACH: Split, reverse, join
    
    WHY THIS WORKS?
    - split() automatically handles multiple spaces
    - Reverse the list of words
    - Join with single space
    
    STEP-BY-STEP:
    1. Split string into words (handles extra spaces)
    2. Reverse the list
    3. Join with single space
    
    TIME: O(n), SPACE: O(n)
    """
    # Method 1: Pythonic
    return ' '.join(reversed(s.split()))
    
    # Method 2: Manual
    words = s.split()
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return ' '.join(words)


# --- EXAMPLE 5: String Compression ---
def string_compression_approach(chars):
    """
    PROBLEM: Compress string in-place. ["a","a","b","b","c","c","c"]
    Output: ["a","2","b","2","c","3"], return 6
    
    APPROACH: Two pointers - read and write
    
    WHY TWO POINTERS?
    - Need to modify in-place
    - Read pointer scans, write pointer places result
    - Count consecutive characters
    
    STEP-BY-STEP:
    1. write pointer at 0
    2. For each character, count consecutive occurrences
    3. Write character at write position
    4. If count > 1, write count digits
    5. Move write pointer
    
    TIME: O(n), SPACE: O(1)
    """
    write = 0
    read = 0
    
    while read < len(chars):
        char = chars[read]
        count = 0
        
        # Count consecutive characters
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        
        # Write character
        chars[write] = char
        write += 1
        
        # Write count if > 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return write


"""
================================================================
COMMON STRING MISTAKES TO AVOID
================================================================

❌ String concatenation in loop (O(n²)):
   result = ""
   for c in s:
       result += c  # BAD!
   
   ✓ Use list + join:
   result = []
   for c in s:
       result.append(c)
   return ''.join(result)

❌ Forgetting strings are immutable:
   s[0] = 'a'  # ERROR!
   
   ✓ Convert to list first:
   chars = list(s)
   chars[0] = 'a'
   s = ''.join(chars)

❌ Not handling case sensitivity:
   "Hello" == "hello"  # False
   
   ✓ Convert to same case:
   s1.lower() == s2.lower()

❌ Not cleaning input for palindrome:
   "A man" != "nam A"
   
   ✓ Remove non-alphanumeric:
   cleaned = ''.join(c.lower() for c in s if c.isalnum())

❌ Off-by-one in slicing:
   s[0:3] includes index 0,1,2 (not 3!)

❌ Not considering empty string:
   if not s: return ...


================================================================
INTERVIEW TIPS FOR STRING PROBLEMS
================================================================

1. CLARIFY INPUT
   - "Is the string ASCII or Unicode?"
   - "Can it be empty?"
   - "Is it case-sensitive?"
   - "Should I ignore spaces/punctuation?"

2. THINK ABOUT PATTERNS
   - Palindrome → Two pointers
   - Anagram → Frequency count
   - Substring → Sliding window
   - Parentheses → Stack
   - Build result → List + join

3. CONSIDER TIME/SPACE TRADEOFFS
   - Sorting: O(n log n) but simple
   - Hash map: O(n) but extra space
   - Two pointers: O(n) and O(1) space

4. TEST WITH EXAMPLES
   - Empty string: ""
   - Single character: "a"
   - All same: "aaaa"
   - Mixed case: "Hello"
   - Special characters: "a!b@c"


================================================================
QUICK REFERENCE
================================================================

PALINDROME:
  → Two pointers from both ends
  → Or compare s == s[::-1]

ANAGRAM:
  → Counter(s1) == Counter(s2)
  → Or sorted(s1) == sorted(s2)

SUBSTRING:
  → Sliding window with set/dict
  → Track window with left/right pointers

STRING BUILDING:
  → Use list + ''.join()
  → NEVER use += in loop

PARENTHESES:
  → Use stack
  → Map closing to opening brackets

CHARACTER CHECKS:
  → c.isalpha(), c.isdigit(), c.isalnum()
  → ord(c), chr(n)
  → c.upper(), c.lower()

Good luck! 🚀
"""

print("\n✅ String theory complete! Now go to problems_easy.py!")

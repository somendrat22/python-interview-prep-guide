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

print("\n✅ String theory complete! Now go to problems_easy.py!")

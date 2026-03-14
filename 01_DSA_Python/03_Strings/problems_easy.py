"""
================================================================
STRINGS — EASY PROBLEMS
================================================================
"""


# ============================================================
# PROBLEM 1: Reverse a String
# ============================================================
"""
PROBLEM (LeetCode 344):
  Given a list of characters, reverse it IN-PLACE.
  
  Input:  ['h', 'e', 'l', 'l', 'o']
  Output: ['o', 'l', 'l', 'e', 'h']

APPROACH: Two Pointers — swap from both ends

VISUAL:
  ['h', 'e', 'l', 'l', 'o']
    L                    R    → swap h,o → ['o', 'e', 'l', 'l', 'h']
         L          R         → swap e,l → ['o', 'l', 'l', 'e', 'h']
              L=R             → STOP (they met)
"""

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 2: Valid Palindrome
# ============================================================
"""
PROBLEM (LeetCode 125):
  Check if a string is a palindrome.
  Consider only alphanumeric characters. Ignore case.
  
  Input:  "A man, a plan, a canal: Panama"
  Output: True  (reads same forwards and backwards: "amanaplanacanalpanama")
  
  Input:  "race a car"
  Output: False

WHAT IS A PALINDROME?
  A word/sentence that reads the same forwards and backwards.
  Examples: "madam", "racecar", "level"

APPROACH: Two Pointers
  - Left pointer starts from beginning
  - Right pointer starts from end
  - Skip non-alphanumeric characters
  - Compare characters (ignoring case)

VISUAL:
  s = "A man, a plan, a canal: Panama"
  
  Clean it first (mentally): "amanaplanacanalpanama"
  
  L→ a ... a ←R  → match ✓
     m ... m      → match ✓
      a ... a     → match ✓
       n ... n    → match ✓
        ... all match → PALINDROME!
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 3: Valid Anagram
# ============================================================
"""
PROBLEM (LeetCode 242):
  Check if string t is an anagram of string s.
  An anagram uses the SAME characters with the SAME frequency, just rearranged.
  
  Input:  s = "anagram", t = "nagaram"
  Output: True
  
  Input:  s = "rat", t = "car"
  Output: False

APPROACH: Count character frequencies
  - Count frequency of each character in s
  - Count frequency of each character in t  
  - If frequencies match → anagram

VISUAL:
  s = "anagram"  → {a:3, n:1, g:1, r:1, m:1}
  t = "nagaram"  → {n:1, a:3, g:1, r:1, m:1}
  Same frequencies → TRUE
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    # Count frequencies
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    for ch in t:
        count[ch] = count.get(ch, 0) - 1
        if count[ch] < 0:   # t has more of this char than s
            return False
    
    return True

# TIME: O(n), SPACE: O(1) — at most 26 letters

# One-liner approach:
# from collections import Counter
# def is_anagram(s, t): return Counter(s) == Counter(t)


# ============================================================
# PROBLEM 4: First Unique Character
# ============================================================
"""
PROBLEM (LeetCode 387):
  Find the FIRST character that appears only ONCE. Return its index.
  If no unique character, return -1.
  
  Input:  "leetcode"
  Output: 0  ('l' is the first unique character)
  
  Input:  "loveleetcode"
  Output: 2  ('v' is the first unique character)
  
  Input:  "aabb"
  Output: -1

APPROACH:
  Step 1: Count frequency of each character
  Step 2: Scan string again, find first char with count == 1

VISUAL:
  s = "loveleetcode"
  Frequencies: {l:1, o:2, v:1, e:4, t:1, c:1, d:1}
  
  Scan left to right:
    s[0]='l' → count=1? No wait, let me recount...
    l:1, o:2, v:1, e:4, l:1... wait l appears again at index 10
    Actually: {l:2, o:2, v:1, e:4, t:1, c:1, d:1}
    
    s[0]='l' → count=2 → skip
    s[1]='o' → count=2 → skip
    s[2]='v' → count=1 → FOUND! Return 2
"""

def first_unique_char(s):
    # Step 1: Count frequencies
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Step 2: Find first char with frequency 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    
    return -1

# TIME: O(n), SPACE: O(1) — at most 26 different characters


# ============================================================
# PROBLEM 5: Longest Common Prefix
# ============================================================
"""
PROBLEM (LeetCode 14):
  Find the longest common prefix among a list of strings.
  
  Input:  ["flower", "flow", "flight"]
  Output: "fl"
  
  Input:  ["dog", "racecar", "car"]
  Output: ""  (no common prefix)

APPROACH: Vertical scanning
  Compare character by character across all strings.
  
  flower
  flow
  flight
  ↓
  f: all have 'f' ✓
  l: all have 'l' ✓
  o/i: 'o' vs 'i' ✗ → STOP! Prefix = "fl"
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Use first string as reference
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Check this character position in all other strings
        for j in range(1, len(strs)):
            # If we've gone past end of another string, or chars don't match
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    
    return strs[0]  # entire first string is the prefix

# TIME: O(S) where S = sum of all characters in all strings
# SPACE: O(1)


# ============================================================
# PROBLEM 6: Count Vowels and Consonants
# ============================================================
"""
PROBLEM:
  Count the number of vowels and consonants in a string.
  Ignore non-alphabetic characters.
  
  Input:  "Hello World"
  Output: Vowels: 3, Consonants: 7

APPROACH: Simple traversal with set lookup
"""

def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0
    
    for ch in s:
        if ch.isalpha():      # is it a letter?
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 7: Check if Two Strings are Rotations of Each Other
# ============================================================
"""
PROBLEM:
  Check if string s2 is a rotation of string s1.
  
  Input:  s1 = "abcde", s2 = "cdeab"
  Output: True  ("abcde" rotated left by 2 = "cdeab")
  
  Input:  s1 = "abcde", s2 = "abced"
  Output: False

TRICK: If s2 is a rotation of s1, then s2 will always be
       a SUBSTRING of s1 + s1!

VISUAL:
  s1 = "abcde"
  s1 + s1 = "abcdeabcde"
  
  Is "cdeab" in "abcdeabcde"?
       Yes! → "abcde|abcde"
                  ↑cdeab↑
  
  So s2 IS a rotation of s1!
"""

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

# TIME: O(n), SPACE: O(n)


# ============================================================
# PROBLEM 8: Remove All Occurrences of a Character
# ============================================================
"""
PROBLEM:
  Remove all occurrences of character c from string s.
  
  Input:  s = "hello world", c = 'l'
  Output: "heo word"
"""

def remove_char(s, c):
    # Method 1: Using replace
    return s.replace(c, "")

    # Method 2: Using list comprehension (more general)
    # return "".join(ch for ch in s if ch != c)

# TIME: O(n), SPACE: O(n) — new string created


# ============================================================
# PROBLEM 9: Check if String Contains Only Digits
# ============================================================
"""
PROBLEM:
  Check if a string is a valid number (only contains digits).
  
  Input:  "12345"  → True
  Input:  "123a5"  → False
  Input:  ""       → False

APPROACH 1: Use built-in isdigit()
APPROACH 2: Manual check using ASCII
"""

def is_number(s):
    if not s:
        return False
    return s.isdigit()

# Manual approach (for understanding):
def is_number_manual(s):
    if not s:
        return False
    for ch in s:
        if not ('0' <= ch <= '9'):  # check ASCII range
            return False
    return True

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 10: Reverse Words in a String
# ============================================================
"""
PROBLEM (LeetCode 151):
  Reverse the order of words in a string.
  
  Input:  "  the sky  is blue  "
  Output: "blue is sky the"
  
  Note: Remove leading/trailing spaces. Single space between words.

APPROACH:
  1. Strip the string
  2. Split by whitespace
  3. Reverse the list of words
  4. Join with single space
"""

def reverse_words(s):
    words = s.split()       # split by any whitespace, ignores extra spaces
    words.reverse()          # reverse the list in-place
    return " ".join(words)   # join with single space

# TIME: O(n), SPACE: O(n)

# One-liner:
# def reverse_words(s): return " ".join(s.split()[::-1])


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TESTING ALL EASY STRING PROBLEMS")
    print("=" * 60)
    
    # Problem 1
    print("\n--- Problem 1: Reverse String ---")
    chars = list("hello")
    print(f"'hello' → {reverse_string(chars)}")  # ['o','l','l','e','h']
    
    # Problem 2
    print("\n--- Problem 2: Valid Palindrome ---")
    print(f"'A man, a plan, a canal: Panama' → {is_palindrome('A man, a plan, a canal: Panama')}")  # True
    print(f"'race a car' → {is_palindrome('race a car')}")  # False
    
    # Problem 3
    print("\n--- Problem 3: Valid Anagram ---")
    print(f"'anagram', 'nagaram' → {is_anagram('anagram', 'nagaram')}")  # True
    print(f"'rat', 'car' → {is_anagram('rat', 'car')}")  # False
    
    # Problem 4
    print("\n--- Problem 4: First Unique Character ---")
    print(f"'leetcode' → {first_unique_char('leetcode')}")  # 0
    print(f"'loveleetcode' → {first_unique_char('loveleetcode')}")  # 2
    print(f"'aabb' → {first_unique_char('aabb')}")  # -1
    
    # Problem 5
    print("\n--- Problem 5: Longest Common Prefix ---")
    print(f"['flower','flow','flight'] → '{longest_common_prefix(['flower','flow','flight'])}'")  # 'fl'
    print(f"['dog','racecar','car'] → '{longest_common_prefix(['dog','racecar','car'])}'")  # ''
    
    # Problem 6
    print("\n--- Problem 6: Count Vowels/Consonants ---")
    v, c = count_vowels_consonants("Hello World")
    print(f"'Hello World' → Vowels: {v}, Consonants: {c}")  # 3, 7
    
    # Problem 7
    print("\n--- Problem 7: String Rotation ---")
    print(f"'abcde', 'cdeab' → {is_rotation('abcde', 'cdeab')}")  # True
    print(f"'abcde', 'abced' → {is_rotation('abcde', 'abced')}")  # False
    
    # Problem 8
    print("\n--- Problem 8: Remove Character ---")
    print(f"'hello world' remove 'l' → '{remove_char('hello world', 'l')}'")  # 'heo word'
    
    # Problem 9
    print("\n--- Problem 9: Is Number ---")
    print(f"'12345' → {is_number('12345')}")  # True
    print(f"'123a5' → {is_number('123a5')}")  # False
    
    # Problem 10
    print("\n--- Problem 10: Reverse Words ---")
    print(f"'  the sky  is blue  ' → '{reverse_words('  the sky  is blue  ')}'")
    # 'blue is sky the'
    
    print("\n✅ All easy string problems done! Move to problems_medium.py")

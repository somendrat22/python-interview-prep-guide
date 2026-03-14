"""
================================================================
STRINGS — MEDIUM PROBLEMS (Interview Level)
================================================================
"""


# ============================================================
# PROBLEM 1: Longest Substring Without Repeating Characters (LeetCode 3)
# ============================================================
"""
PROBLEM:
  Find the length of the longest substring without repeating characters.
  
  Input:  "abcabcbb"
  Output: 3  (substring "abc")
  
  Input:  "bbbbb"
  Output: 1  (substring "b")
  
  Input:  "pwwkew"
  Output: 3  (substring "wke")

APPROACH: Sliding Window
  - Maintain a window [left, right] with no duplicates
  - Use a set to track characters in current window
  - Expand right pointer: if char not in set, add it
  - If char IS in set: shrink from left until duplicate removed

VISUAL:
  s = "abcabcbb"
  
  Window: [a]bcabcbb     → set={a}, len=1
  Window: [ab]cabcbb     → set={a,b}, len=2
  Window: [abc]abcbb     → set={a,b,c}, len=3
  Window: [abc]a → 'a' already in set!
          Remove from left: remove 'a' → set={b,c}
  Window: b[bca]bcbb     → set={b,c,a}, len=3
  ... and so on
  
  Max length = 3
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to window
        char_set.add(s[right])
        
        # Update max length
        max_len = max(max_len, right - left + 1)
    
    return max_len

# TIME: O(n) — each character is added and removed at most once
# SPACE: O(min(n, 26)) — at most 26 lowercase letters in set


# ============================================================
# PROBLEM 2: Group Anagrams (LeetCode 49)
# ============================================================
"""
PROBLEM:
  Group strings that are anagrams of each other.
  
  Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
  Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

APPROACH:
  Anagrams have the same characters → same SORTED string!
  "eat" sorted = "aet"
  "tea" sorted = "aet"  → same group!
  "tan" sorted = "ant"
  "nat" sorted = "ant"  → same group!
  
  Use sorted string as dictionary KEY, group words by key.
"""

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        key = "".join(sorted(s))   # sort characters → anagram key
        groups[key].append(s)
    
    return list(groups.values())

# TIME: O(n * k log k) where n = number of strings, k = max string length
# SPACE: O(n * k)


# ============================================================
# PROBLEM 3: Longest Palindromic Substring (LeetCode 5)
# ============================================================
"""
PROBLEM:
  Find the longest substring that is a palindrome.
  
  Input:  "babad"
  Output: "bab" (or "aba" — both valid)
  
  Input:  "cbbd"
  Output: "bb"

APPROACH: Expand Around Center
  A palindrome mirrors around its center.
  For each position, try to expand outward while characters match.
  
  Two cases:
    - Odd length palindrome: center is one character  (e.g., "aba")
    - Even length palindrome: center is between two characters (e.g., "abba")

VISUAL:
  s = "babad"
  
  Center at 'b'(0): expand → "b" (len 1)
  Center at 'a'(1): expand → "a" → "bab" (len 3) ✓
  Center at 'b'(2): expand → "b" → "aba" (len 3)
  Center at 'a'(3): expand → "a" (len 1)
  Center at 'd'(4): expand → "d" (len 1)
  
  Longest = "bab" (length 3)
"""

def longest_palindrome(s):
    if len(s) < 2:
        return s
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        """Expand outward while characters match."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # When loop ends, s[left+1:right] is the palindrome
        return right - left - 1  # length of palindrome
    
    for i in range(len(s)):
        # Odd length palindrome (center = single char)
        len1 = expand_around_center(i, i)
        # Even length palindrome (center = between two chars)
        len2 = expand_around_center(i, i + 1)
        
        curr_max = max(len1, len2)
        if curr_max > max_len:
            max_len = curr_max
            start = i - (curr_max - 1) // 2
    
    return s[start:start + max_len]

# TIME: O(n²) — for each center, expand can take O(n)
# SPACE: O(1)


# ============================================================
# PROBLEM 4: String to Integer (atoi) (LeetCode 8)
# ============================================================
"""
PROBLEM:
  Implement atoi: convert a string to an integer.
  
  Rules:
  1. Discard leading whitespace
  2. Check for +/- sign
  3. Read digits until non-digit or end
  4. Clamp to 32-bit integer range [-2^31, 2^31 - 1]
  
  Input:  "   -42"     → -42
  Input:  "4193 word"  → 4193
  Input:  "words 987"  → 0 (first non-space is not digit/sign)

APPROACH: Process character by character
"""

def my_atoi(s):
    s = s.strip()       # Step 1: remove leading/trailing whitespace
    if not s:
        return 0
    
    sign = 1
    i = 0
    result = 0
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -(2**31)   # -2147483648
    
    # Step 2: check for sign
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    # Step 3: read digits
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        
        # Step 4: check for overflow BEFORE adding digit
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1
    
    return sign * result

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 5: Count and Say (LeetCode 38)
# ============================================================
"""
PROBLEM:
  Generate the nth term of the "count and say" sequence.
  
  1  → "1"              (start)
  2  → "11"             (one 1)
  3  → "21"             (two 1s)
  4  → "1211"           (one 2, one 1)
  5  → "111221"         (one 1, one 2, two 1s)
  
  Each term DESCRIBES the previous term.
  "21" means: "two 1s" → that's what "111221" is NOT.
  Wait, let me re-explain:
    "1"    → read it: "one 1"       → write: "11"
    "11"   → read it: "two 1s"      → write: "21"
    "21"   → read it: "one 2, one 1"→ write: "1211"
    "1211" → read it: "one 1, one 2, two 1s" → write: "111221"
"""

def count_and_say(n):
    result = "1"
    
    for _ in range(n - 1):
        new_result = []
        i = 0
        while i < len(result):
            # Count consecutive same characters
            count = 1
            while i + count < len(result) and result[i + count] == result[i]:
                count += 1
            new_result.append(str(count) + result[i])
            i += count
        result = "".join(new_result)
    
    return result

# TIME: O(n * m) where m = length of the string at each step
# SPACE: O(m)


# ============================================================
# PROBLEM 6: Implement strStr() / Find Needle in Haystack (LeetCode 28)
# ============================================================
"""
PROBLEM:
  Find the first occurrence of 'needle' in 'haystack'.
  Return the index, or -1 if not found.
  
  Input:  haystack = "sadbutsad", needle = "sad"
  Output: 0
  
  Input:  haystack = "leetcode", needle = "leeto"
  Output: -1

APPROACH: Sliding window of needle's length
"""

def str_str(haystack, needle):
    if not needle:
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):
        # Check if substring starting at i matches needle
        if haystack[i:i+m] == needle:
            return i
    
    return -1

# TIME: O(n * m) worst case
# SPACE: O(m) for the slice comparison

# Pythonic: return haystack.find(needle)


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TESTING ALL MEDIUM STRING PROBLEMS")
    print("=" * 60)
    
    print("\n--- Problem 1: Longest Substring Without Repeating ---")
    print(f"'abcabcbb' → {length_of_longest_substring('abcabcbb')}")  # 3
    print(f"'bbbbb' → {length_of_longest_substring('bbbbb')}")  # 1
    print(f"'pwwkew' → {length_of_longest_substring('pwwkew')}")  # 3
    
    print("\n--- Problem 2: Group Anagrams ---")
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    for group in result:
        print(f"  {group}")
    
    print("\n--- Problem 3: Longest Palindromic Substring ---")
    print(f"'babad' → '{longest_palindrome('babad')}'")  # 'bab' or 'aba'
    print(f"'cbbd' → '{longest_palindrome('cbbd')}'")    # 'bb'
    
    print("\n--- Problem 4: String to Integer (atoi) ---")
    print(f"'   -42' → {my_atoi('   -42')}")        # -42
    print(f"'4193 word' → {my_atoi('4193 word')}")   # 4193
    print(f"'words 987' → {my_atoi('words 987')}")   # 0
    
    print("\n--- Problem 5: Count and Say ---")
    for i in range(1, 7):
        print(f"  n={i}: '{count_and_say(i)}'")
    
    print("\n--- Problem 6: strStr ---")
    print(f"'sadbutsad','sad' → {str_str('sadbutsad', 'sad')}")  # 0
    print(f"'leetcode','leeto' → {str_str('leetcode', 'leeto')}")  # -1
    
    print("\n✅ All medium string problems done!")

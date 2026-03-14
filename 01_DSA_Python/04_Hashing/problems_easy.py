"""
================================================================
HASHING — EASY PROBLEMS
================================================================
"""


# ============================================================
# PROBLEM 1: Two Sum (Using HashMap) — LeetCode 1
# ============================================================
"""
PROBLEM:
  Given array nums and target, find two numbers that add up to target.
  Return their indices.
  
  Input:  nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]

WHY HASHING?
  - Brute force: check every pair → O(n²)
  - With hash map: for each number, check if (target - number) exists → O(n)

VISUAL:
  nums = [2, 7, 11, 15], target = 9
  seen = {}
  
  num=2:  need 9-2=7.  Is 7 in seen? NO.  Add {2: 0}
  num=7:  need 9-7=2.  Is 2 in seen? YES! Return [seen[2], 1] = [0, 1]
"""

def two_sum(nums, target):
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# TIME: O(n), SPACE: O(n)


# ============================================================
# PROBLEM 2: Contains Duplicate — LeetCode 217
# ============================================================
"""
PROBLEM:
  Return True if any value appears at least TWICE in the array.
  
  Input:  [1, 2, 3, 1]  → True
  Input:  [1, 2, 3, 4]  → False

WHY HASHING?
  Use a SET to track seen numbers. If we try to add a number
  that's already in the set → duplicate found!
"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:      # O(1) lookup!
            return True
        seen.add(num)
    return False

# TIME: O(n), SPACE: O(n)

# One-liner:
# def contains_duplicate(nums): return len(nums) != len(set(nums))


# ============================================================
# PROBLEM 3: Valid Anagram — LeetCode 242
# ============================================================
"""
PROBLEM:
  Check if t is an anagram of s (same characters, same frequency).
  
  Input:  s = "anagram", t = "nagaram"  → True
  Input:  s = "rat", t = "car"          → False

APPROACH: Count frequency with dict, compare.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        count[ch] = count.get(ch, 0) - 1
        if count[ch] < 0:
            return False
    return True

# TIME: O(n), SPACE: O(1) — at most 26 letters


# ============================================================
# PROBLEM 4: Intersection of Two Arrays — LeetCode 349
# ============================================================
"""
PROBLEM:
  Find the intersection (common elements) of two arrays.
  Each element in the result must be UNIQUE.
  
  Input:  nums1 = [1,2,2,1], nums2 = [2,2]
  Output: [2]
  
  Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  Output: [9,4]

APPROACH: Convert to sets, use set intersection.
"""

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# TIME: O(n + m), SPACE: O(n + m)


# ============================================================
# PROBLEM 5: Find All Numbers Disappeared in an Array — LeetCode 448
# ============================================================
"""
PROBLEM:
  Array of n integers where each is in range [1, n].
  Some numbers appear twice, some don't appear.
  Find all numbers that DON'T appear.
  
  Input:  [4, 3, 2, 7, 8, 2, 3, 1]  (n=8, range 1-8)
  Output: [5, 6]

APPROACH: Put all numbers in a set, check which 1..n are missing.
"""

def find_disappeared_numbers(nums):
    num_set = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in num_set]

# TIME: O(n), SPACE: O(n)


# ============================================================
# PROBLEM 6: Single Number — LeetCode 136
# ============================================================
"""
PROBLEM:
  Every element appears twice except one. Find the single one.
  
  Input:  [2, 2, 1]        → 1
  Input:  [4, 1, 2, 1, 2]  → 4

APPROACH 1: Hash Set — add if not seen, remove if seen
APPROACH 2: XOR (more optimal, O(1) space)
"""

# Hash Set approach (easy to understand):
def single_number_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)   # appeared twice → remove
        else:
            seen.add(num)      # first time → add
    return seen.pop()           # only the single number remains

# XOR approach (optimal):
def single_number_xor(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Both: TIME: O(n). Set: SPACE O(n), XOR: SPACE O(1)


# ============================================================
# PROBLEM 7: Majority Element — LeetCode 169
# ============================================================
"""
PROBLEM:
  Find the element that appears more than n/2 times.
  (It's guaranteed to exist.)
  
  Input:  [3, 2, 3]        → 3
  Input:  [2, 2, 1, 1, 1, 2, 2]  → 2

APPROACH: Count with dict, find max count.
"""

from collections import Counter

def majority_element(nums):
    count = Counter(nums)
    return max(count.keys(), key=count.get)

# TIME: O(n), SPACE: O(n)

# Optimal: Boyer-Moore Voting Algorithm (O(1) space)
def majority_element_optimal(nums):
    """
    Idea: The majority element can "survive" cancellation with all others.
    """
    candidate = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1
    return candidate


# ============================================================
# PROBLEM 8: Roman to Integer — LeetCode 13
# ============================================================
"""
PROBLEM:
  Convert a Roman numeral string to an integer.
  
  I=1, V=5, X=10, L=50, C=100, D=500, M=1000
  
  Special cases: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
  (When a smaller value is BEFORE a larger value, subtract it)
  
  Input:  "III"     → 3
  Input:  "LVIII"   → 58  (L=50 + V=5 + III=3)
  Input:  "MCMXCIV" → 1994 (M=1000 + CM=900 + XC=90 + IV=4)

APPROACH: Use a dict for values. If current < next → subtract, else add.
"""

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
             'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(s)):
        # If current value < next value → subtract (e.g., IV = -1 + 5 = 4)
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    
    return result

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 9: Word Pattern — LeetCode 290
# ============================================================
"""
PROBLEM:
  Check if string s follows pattern.
  
  Input:  pattern = "abba", s = "dog cat cat dog"  → True
  Input:  pattern = "abba", s = "dog cat cat fish" → False
  Input:  pattern = "aaaa", s = "dog cat cat dog"  → False

  Each letter in pattern maps to exactly one word (and vice versa).

APPROACH: Use TWO dicts for bidirectional mapping.
"""

def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for ch, word in zip(pattern, words):
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            char_to_word[ch] = word
        
        if word in word_to_char:
            if word_to_char[word] != ch:
                return False
        else:
            word_to_char[word] = ch
    
    return True

# TIME: O(n), SPACE: O(n)


# ============================================================
# PROBLEM 10: Isomorphic Strings — LeetCode 205
# ============================================================
"""
PROBLEM:
  Two strings are isomorphic if characters in s can be replaced to get t.
  No two characters may map to the same character, and mapping must be consistent.
  
  Input:  s = "egg", t = "add"    → True  (e→a, g→d)
  Input:  s = "foo", t = "bar"    → False (o maps to both a and r)
  Input:  s = "paper", t = "title" → True (p→t, a→i, e→l, r→e)

APPROACH: Same as word pattern — bidirectional mapping.
"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for ch_s, ch_t in zip(s, t):
        if ch_s in s_to_t:
            if s_to_t[ch_s] != ch_t:
                return False
        else:
            s_to_t[ch_s] = ch_t
        
        if ch_t in t_to_s:
            if t_to_s[ch_t] != ch_s:
                return False
        else:
            t_to_s[ch_t] = ch_s
    
    return True

# TIME: O(n), SPACE: O(1) — at most 256 characters


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TESTING ALL EASY HASHING PROBLEMS")
    print("=" * 60)
    
    print("\n--- Problem 1: Two Sum ---")
    print(f"[2,7,11,15] target=9 → {two_sum([2,7,11,15], 9)}")
    
    print("\n--- Problem 2: Contains Duplicate ---")
    print(f"[1,2,3,1] → {contains_duplicate([1,2,3,1])}")
    print(f"[1,2,3,4] → {contains_duplicate([1,2,3,4])}")
    
    print("\n--- Problem 3: Valid Anagram ---")
    print(f"'anagram','nagaram' → {is_anagram('anagram','nagaram')}")
    print(f"'rat','car' → {is_anagram('rat','car')}")
    
    print("\n--- Problem 4: Intersection ---")
    print(f"[1,2,2,1] & [2,2] → {intersection([1,2,2,1],[2,2])}")
    
    print("\n--- Problem 5: Disappeared Numbers ---")
    print(f"[4,3,2,7,8,2,3,1] → {find_disappeared_numbers([4,3,2,7,8,2,3,1])}")
    
    print("\n--- Problem 6: Single Number ---")
    print(f"[4,1,2,1,2] → {single_number_xor([4,1,2,1,2])}")
    
    print("\n--- Problem 7: Majority Element ---")
    print(f"[2,2,1,1,1,2,2] → {majority_element([2,2,1,1,1,2,2])}")
    
    print("\n--- Problem 8: Roman to Integer ---")
    print(f"'MCMXCIV' → {roman_to_int('MCMXCIV')}")
    
    print("\n--- Problem 9: Word Pattern ---")
    print(f"'abba','dog cat cat dog' → {word_pattern('abba','dog cat cat dog')}")
    print(f"'abba','dog cat cat fish' → {word_pattern('abba','dog cat cat fish')}")
    
    print("\n--- Problem 10: Isomorphic ---")
    print(f"'egg','add' → {is_isomorphic('egg','add')}")
    print(f"'foo','bar' → {is_isomorphic('foo','bar')}")
    
    print("\n✅ All easy hashing problems done!")

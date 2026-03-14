"""
================================================================
TOPIC 5: TWO POINTERS & SLIDING WINDOW — Complete Beginner Guide
================================================================

These are TECHNIQUES (not data structures). They are patterns
you use to solve array/string problems efficiently.

================================================================
SECTION 1: TWO POINTERS TECHNIQUE
================================================================

WHAT IS IT?
  Use TWO variables (pointers) that move through the data structure,
  usually from different positions or at different speeds.

WHY USE IT?
  - Turns O(n²) brute force into O(n)
  - Works on SORTED arrays and strings

THREE TYPES OF TWO POINTERS:

  TYPE 1: Opposite Direction (Start & End)
    Left starts at beginning, Right starts at end, move inward.
    Use for: Palindromes, Pair sum in sorted array, Container with water
    
    [1, 2, 3, 4, 5, 6, 7]
     L→                ←R
    
  TYPE 2: Same Direction (Slow & Fast)
    Both start at beginning, move at different speeds.
    Use for: Remove duplicates, Linked list cycle, Partition
    
    [1, 1, 2, 2, 3, 3, 4]
     S→
     F→→→
    
  TYPE 3: Two Arrays
    One pointer for each array.
    Use for: Merge sorted arrays, Intersection
    
    [1, 3, 5, 7]     [2, 4, 6, 8]
     ↑                 ↑
"""


# ============================================================
# TYPE 1: OPPOSITE DIRECTION EXAMPLES
# ============================================================

# --- Example 1: Pair with Target Sum in Sorted Array ---
"""
PROBLEM:
  Given a SORTED array, find two numbers that add up to target.
  
  Input:  [1, 2, 3, 4, 6], target = 6
  Output: [1, 3]  (indices, because 2 + 4 = 6)

WHY TWO POINTERS WORK HERE:
  Array is SORTED. If sum is too big → move right pointer left (decrease sum).
  If sum is too small → move left pointer right (increase sum).

VISUAL:
  [1, 2, 3, 4, 6], target = 6
   L              R   → 1+6=7 > 6 → move R left
   L           R      → 1+4=5 < 6 → move L right
      L        R      → 2+4=6 = 6 → FOUND! [1, 3]
"""

def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1       # need bigger sum → move left forward
        else:
            right -= 1      # need smaller sum → move right backward
    
    return []

# TIME: O(n), SPACE: O(1)


# --- Example 2: Three Sum (LeetCode 15) ---
"""
PROBLEM:
  Find all unique triplets that sum to zero.
  
  Input:  [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]

APPROACH:
  1. Sort the array
  2. Fix one element (i), use two pointers on the rest
  3. Skip duplicates

VISUAL:
  Sorted: [-4, -1, -1, 0, 1, 2]
  
  Fix -4: find pairs in [-1,-1,0,1,2] that sum to 4 → none
  Fix -1: find pairs in [-1,0,1,2] that sum to 1
          → L=-1, R=2: -1+2=1 → FOUND [-1, -1, 2]
          → L=0, R=1: 0+1=1 → FOUND [-1, 0, 1]
  Fix -1: skip (same as previous)
  ...
"""

def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

# TIME: O(n²), SPACE: O(1) excluding output


# ============================================================
# TYPE 2: SAME DIRECTION (SLOW & FAST)
# ============================================================

# --- Example: Remove Duplicates from Sorted Array ---
"""
PROBLEM (LeetCode 26):
  Remove duplicates in-place from sorted array. Return new length.
  
  Input:  [1, 1, 2, 2, 3]
  Output: 3 (array becomes [1, 2, 3, ...])

VISUAL:
  [1, 1, 2, 2, 3]
   S  F              → arr[F]=1 == arr[S]=1 → just move F
   S     F           → arr[F]=2 != arr[S]=1 → S++, arr[S]=2
      S     F        → arr[F]=2 == arr[S]=2 → just move F
      S        F     → arr[F]=3 != arr[S]=2 → S++, arr[S]=3
  
  Result: [1, 2, 3, _, _], return S+1 = 3
"""

def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0  # points to last unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# TIME: O(n), SPACE: O(1)


# ============================================================
# SECTION 2: SLIDING WINDOW TECHNIQUE
# ============================================================
"""
WHAT IS IT?
  A "window" is a contiguous subarray/substring.
  Instead of recalculating from scratch, we SLIDE the window
  by adding one element and removing one element.

WHY USE IT?
  - Problems about contiguous subarrays/substrings
  - Turns O(n*k) into O(n) for window of size k

TWO TYPES:

  TYPE 1: FIXED SIZE WINDOW
    Window size is given (e.g., "max sum of subarray of size k")
    
    [1, 3, 2, 6, -1, 4, 1, 8, 2]
    |___k=3__|
       |___k=3__|
          |___k=3__|    → slide by removing left, adding right
    
  TYPE 2: VARIABLE SIZE WINDOW
    Window size changes based on condition
    (e.g., "smallest subarray with sum >= target")
    
    [2, 1, 5, 2, 3, 2]
    |__|          → too small, expand right
    |_____|       → big enough, try shrink from left
       |__|       → too small, expand right
"""


# ============================================================
# FIXED SIZE WINDOW
# ============================================================

# --- Example: Maximum Sum of Subarray of Size K ---
"""
PROBLEM:
  Find the maximum sum of any contiguous subarray of size k.
  
  Input:  arr = [2, 1, 5, 1, 3, 2], k = 3
  Output: 9  (subarray [5, 1, 3])

BRUTE FORCE: For each starting position, sum k elements → O(n*k)

SLIDING WINDOW: 
  1. Calculate sum of first k elements
  2. Slide: subtract leftmost, add next element
  
VISUAL:
  arr = [2, 1, 5, 1, 3, 2], k = 3
  
  Window [2, 1, 5]: sum = 8
  Slide → remove 2, add 1: [1, 5, 1]: sum = 8-2+1 = 7
  Slide → remove 1, add 3: [5, 1, 3]: sum = 7-1+3 = 9 ← MAX
  Slide → remove 5, add 2: [1, 3, 2]: sum = 9-5+2 = 6
  
  Answer: 9
"""

def max_sum_subarray_k(arr, k):
    if len(arr) < k:
        return -1
    
    # Step 1: Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i]        # add new element (right side)
        window_sum -= arr[i - k]    # remove old element (left side)
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# TIME: O(n), SPACE: O(1)


# ============================================================
# VARIABLE SIZE WINDOW
# ============================================================

# --- Example: Smallest Subarray with Sum >= Target (LeetCode 209) ---
"""
PROBLEM:
  Find the minimum length of a contiguous subarray whose sum >= target.
  If no such subarray exists, return 0.
  
  Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
  Output: 2  (subarray [4, 3] has sum 7)

APPROACH:
  - Expand window (move right pointer) until sum >= target
  - Then shrink window (move left pointer) to find minimum length
  - Repeat

VISUAL:
  target = 7, nums = [2, 3, 1, 2, 4, 3]
  
  [2]             sum=2 < 7 → expand
  [2,3]           sum=5 < 7 → expand
  [2,3,1]         sum=6 < 7 → expand
  [2,3,1,2]       sum=8 >= 7 → found! len=4. Try shrink.
    [3,1,2]       sum=6 < 7 → expand
    [3,1,2,4]     sum=10 >= 7 → found! len=4. Try shrink.
      [1,2,4]     sum=7 >= 7 → found! len=3. Try shrink.
        [2,4]     sum=6 < 7 → expand
        [2,4,3]   sum=9 >= 7 → found! len=3. Try shrink.
          [4,3]   sum=7 >= 7 → found! len=2. Try shrink.
            [3]   sum=3 < 7 → end
  
  Answer: 2
"""

def min_subarray_len(target, nums):
    min_len = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]           # expand window
        
        while window_sum >= target:          # try to shrink
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# TIME: O(n) — each element is added/removed at most once
# SPACE: O(1)


# --- Example: Longest Substring Without Repeating Characters (LeetCode 3) ---
"""
PROBLEM:
  Find the length of the longest substring without repeating characters.
  
  Input:  "abcabcbb"
  Output: 3  ("abc")
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# TIME: O(n), SPACE: O(min(n, 26))


# --- Example: Maximum Average Subarray (LeetCode 643) ---
"""
PROBLEM:
  Find contiguous subarray of length k with maximum average.
  
  Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
  Output: 12.75  (subarray [12, -5, -6, 50] → sum=51, avg=12.75)
"""

def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k

# TIME: O(n), SPACE: O(1)


# ============================================================
# HOW TO IDENTIFY WHICH TECHNIQUE TO USE
# ============================================================
"""
USE TWO POINTERS WHEN:
  ✓ Array is SORTED
  ✓ Finding pairs/triplets with a target sum
  ✓ Removing duplicates in-place
  ✓ Reversing array/string
  ✓ Palindrome checking

USE SLIDING WINDOW WHEN:
  ✓ "Contiguous subarray/substring"
  ✓ "Maximum/minimum sum/length of subarray"
  ✓ "Substring with certain property"
  ✓ Fixed-size window problems
  ✓ Variable-size window with a condition

COMMON MISTAKES:
  ✗ Using sliding window on unsorted array for pair sum (use hashing)
  ✗ Forgetting to handle edge cases (empty array, k > n)
  ✗ Not shrinking the window when you should
"""


# ============================================================
# RUN ALL EXAMPLES
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TWO POINTERS & SLIDING WINDOW EXAMPLES")
    print("=" * 60)
    
    print("\n--- Two Pointers: Pair Sum (Sorted) ---")
    print(f"[1,2,3,4,6] target=6 → {pair_with_target_sum([1,2,3,4,6], 6)}")
    
    print("\n--- Two Pointers: Three Sum ---")
    print(f"[-1,0,1,2,-1,-4] → {three_sum([-1,0,1,2,-1,-4])}")
    
    print("\n--- Two Pointers: Remove Duplicates ---")
    arr = [1, 1, 2, 2, 3]
    k = remove_duplicates(arr)
    print(f"[1,1,2,2,3] → {k} unique: {arr[:k]}")
    
    print("\n--- Fixed Window: Max Sum of Size K ---")
    print(f"[2,1,5,1,3,2] k=3 → {max_sum_subarray_k([2,1,5,1,3,2], 3)}")
    
    print("\n--- Variable Window: Min Subarray Sum >= Target ---")
    print(f"target=7, [2,3,1,2,4,3] → {min_subarray_len(7, [2,3,1,2,4,3])}")
    
    print("\n--- Variable Window: Longest Substring No Repeat ---")
    print(f"'abcabcbb' → {length_of_longest_substring('abcabcbb')}")
    
    print("\n--- Fixed Window: Max Average Subarray ---")
    print(f"[1,12,-5,-6,50,3] k=4 → {find_max_average([1,12,-5,-6,50,3], 4)}")
    
    print("\n✅ Two Pointers & Sliding Window theory complete!")

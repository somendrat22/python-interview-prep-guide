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


# ============================================================
# QUESTION APPROACH GUIDE — DETAILED EXPLANATIONS
# ============================================================
"""
================================================================
HOW TO IDENTIFY TWO POINTERS VS SLIDING WINDOW
================================================================

ASK YOURSELF:

1. Is the array/string SORTED?
   → YES: Consider Two Pointers (opposite direction)
   → NO: Consider Sliding Window or Hashing

2. Am I looking for PAIRS/TRIPLETS with a condition?
   → Two Pointers (if sorted)
   → Hashing (if unsorted)

3. Am I looking for a CONTIGUOUS SUBARRAY/SUBSTRING?
   → Sliding Window

4. Do I need to REMOVE/MOVE elements IN-PLACE?
   → Two Pointers (same direction - slow/fast)

5. Is there a FIXED WINDOW SIZE?
   → Sliding Window (fixed size)

6. Is there a VARIABLE WINDOW with a condition?
   → Sliding Window (variable size)


================================================================
DETAILED PROBLEM-SOLVING APPROACHES
================================================================
"""


# --- APPROACH 1: Two Sum (Sorted Array) ---
def two_sum_sorted_detailed(numbers, target):
    """
    PROBLEM: Find two numbers in SORTED array that add to target.
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2] (1-indexed)
    
    WHY TWO POINTERS?
    - Array is SORTED - this is the key!
    - If sum is too small, move left pointer right (increase sum)
    - If sum is too large, move right pointer left (decrease sum)
    - This eliminates half the search space each step
    
    WHY NOT HASHING?
    - Two pointers is O(1) space vs O(n) for hash map
    - Sorted array enables this optimization
    
    STEP-BY-STEP:
    1. left = 0, right = n-1
    2. Calculate sum = numbers[left] + numbers[right]
    3. If sum == target: found!
    4. If sum < target: need bigger sum → left++
    5. If sum > target: need smaller sum → right--
    6. Repeat until found or pointers meet
    
    TIME: O(n), SPACE: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1  # need larger sum
        else:
            right -= 1  # need smaller sum
    
    return []


# --- APPROACH 2: Container With Most Water ---
def max_area_detailed(height):
    """
    PROBLEM: Find two lines that form container with most water.
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49 (lines at index 1 and 8)
    
    WHY TWO POINTERS?
    - Start with widest container (left=0, right=n-1)
    - Area = min(height[left], height[right]) * width
    - To potentially increase area, move the SHORTER line
    - Why? Moving taller line can only decrease area
    
    INTUITION:
    - Width decreases as pointers move inward
    - To compensate, we need taller lines
    - Always move the shorter line hoping for a taller one
    
    STEP-BY-STEP:
    1. Start with left=0, right=n-1 (maximum width)
    2. Calculate area = min(height[left], height[right]) * (right - left)
    3. Track maximum area
    4. Move the pointer with shorter height inward
    5. Repeat until pointers meet
    
    TIME: O(n), SPACE: O(1)
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        
        # Move the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


# --- APPROACH 3: Remove Duplicates from Sorted Array ---
def remove_duplicates_detailed(nums):
    """
    PROBLEM: Remove duplicates in-place from sorted array.
    Input: nums = [1,1,2,2,3]
    Output: 3, nums = [1,2,3,_,_]
    
    WHY TWO POINTERS (SLOW/FAST)?
    - Need to modify in-place (can't use extra space)
    - Slow pointer: position for next unique element
    - Fast pointer: scans through array
    
    VISUALIZATION:
    [1, 1, 2, 2, 3]
     S  F              → nums[F]=1 == nums[S]=1, just move F
     S     F           → nums[F]=2 != nums[S]=1, S++, nums[S]=2
        S     F        → nums[F]=2 == nums[S]=2, just move F
        S        F     → nums[F]=3 != nums[S]=2, S++, nums[S]=3
    Result: [1, 2, 3, _, _], return S+1 = 3
    
    STEP-BY-STEP:
    1. slow = 0 (position for next unique)
    2. fast scans from 1 to n-1
    3. If nums[fast] != nums[slow]:
       - Found new unique element
       - slow++
       - nums[slow] = nums[fast]
    4. Return slow + 1 (count of unique elements)
    
    TIME: O(n), SPACE: O(1)
    """
    if not nums:
        return 0
    
    slow = 0
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


# --- APPROACH 4: Longest Substring Without Repeating ---
def length_longest_substring_detailed(s):
    """
    PROBLEM: Find length of longest substring without repeating characters.
    Input: s = "abcabcbb"
    Output: 3 ("abc")
    
    WHY SLIDING WINDOW?
    - Need CONTIGUOUS substring
    - Condition: no repeating characters
    - Window size varies based on condition
    
    VISUALIZATION:
    "abcabcbb"
     L→R          → "a" valid, len=1
     L→→R         → "ab" valid, len=2
     L→→→R        → "abc" valid, len=3
     L→→→→R       → "abca" invalid! 'a' repeats
       L→→R       → shrink: "bca" valid, len=3
       L→→→R      → "bcab" invalid! 'b' repeats
         L→R      → shrink: "cab" valid, len=3
    
    STEP-BY-STEP:
    1. Use set to track characters in current window
    2. Expand right pointer, add character
    3. If duplicate found:
       - Shrink from left until duplicate removed
    4. Track maximum window size
    
    KEY INSIGHT:
    - Set provides O(1) lookup for duplicates
    - Shrink window by removing from left
    
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


# --- APPROACH 5: Minimum Window Substring ---
def min_window_detailed(s, t):
    """
    PROBLEM: Find minimum window in s that contains all characters of t.
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    
    WHY SLIDING WINDOW?
    - Need contiguous substring
    - Variable size window
    - Condition: contains all characters of t
    
    APPROACH:
    1. Expand window until all characters of t are included
    2. Shrink window while still valid to find minimum
    3. Repeat
    
    TRACKING:
    - need: Counter of characters needed from t
    - have: Counter of characters in current window
    - formed: count of unique characters that meet requirement
    
    STEP-BY-STEP:
    1. Count characters needed from t
    2. Expand right:
       - Add character to window
       - If character count matches need, increment formed
    3. While window is valid (formed == required):
       - Update result if smaller
       - Shrink from left
       - If character count drops below need, decrement formed
    
    TIME: O(|s| + |t|), SPACE: O(|s| + |t|)
    """
    from collections import Counter
    
    if not s or not t:
        return ""
    
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
        
        # Check if this character's requirement is met
        if char in need and have[char] == need[char]:
            formed += 1
        
        # Try to shrink window while valid
        while formed == required:
            # Update result if smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]
            
            # Shrink from left
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    
    return result


# --- APPROACH 6: Trapping Rain Water ---
def trap_rain_water_detailed(height):
    """
    PROBLEM: Calculate how much rain water can be trapped.
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    
    WHY TWO POINTERS?
    - Water at position i = min(max_left, max_right) - height[i]
    - Use two pointers to track max heights from both sides
    
    KEY INSIGHT:
    - Water level at any position depends on the MINIMUM of:
      - Maximum height to its left
      - Maximum height to its right
    - We can process from both ends simultaneously
    
    APPROACH:
    1. Start with left=0, right=n-1
    2. Track max_left and max_right
    3. Move pointer with smaller max height
    4. Calculate water at that position
    
    WHY THIS WORKS:
    - If max_left < max_right:
      - Water at left is limited by max_left
      - We know max_right is taller, so max_left is the bottleneck
    - Vice versa for right side
    
    TIME: O(n), SPACE: O(1)
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    max_left = max_right = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            # Process left side
            if height[left] >= max_left:
                max_left = height[left]
            else:
                water += max_left - height[left]
            left += 1
        else:
            # Process right side
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1
    
    return water


"""
================================================================
COMMON MISTAKES TO AVOID
================================================================

❌ Using sliding window on UNSORTED array for pair sum:
   - Sliding window doesn't work for pair sum unless sorted
   - Use hashing for unsorted arrays

❌ Forgetting to shrink the window:
   - In variable-size sliding window, must shrink when condition violated
   - Use while loop to shrink, not if

❌ Wrong pointer movement in two pointers:
   - For pair sum: move left if sum too small, right if too large
   - For container: move the SHORTER height

❌ Not handling edge cases:
   - Empty array/string
   - Single element
   - All same elements

❌ Off-by-one errors:
   - Window size = right - left + 1 (not right - left)
   - Be careful with inclusive/exclusive bounds

❌ Using wrong data structure for window:
   - Use set for unique elements
   - Use dict/Counter for frequency
   - Use deque for sliding window maximum


================================================================
INTERVIEW TIPS
================================================================

1. IDENTIFY THE PATTERN
   "I see this is a sorted array, so two pointers would work..."
   "This asks for a contiguous substring, so sliding window..."
   "We need to remove duplicates in-place, so slow/fast pointers..."

2. EXPLAIN YOUR APPROACH
   "I'll use two pointers starting from both ends..."
   "The window will expand right and shrink left when..."
   "We track the window with a set/dict to..."

3. DISCUSS COMPLEXITY
   "This is O(n) because each element is visited at most twice..."
   "Space is O(1) since we only use two pointers..."
   "We could use hashing but that would be O(n) space..."

4. TEST WITH EXAMPLES
   Walk through with a small example
   Check edge cases: empty, single element, all same

5. OPTIMIZE IF ASKED
   "We could optimize space by using two pointers instead of hash map..."
   "If the array were sorted, we could use two pointers..."


================================================================
QUICK DECISION TREE
================================================================

START HERE:
  ↓
Is array/string SORTED?
  ↓ YES → Two Pointers (opposite direction)
  ↓ NO  → Continue
  ↓
Need CONTIGUOUS subarray/substring?
  ↓ YES → Sliding Window
  ↓ NO  → Continue
  ↓
Need to modify IN-PLACE?
  ↓ YES → Two Pointers (slow/fast)
  ↓ NO  → Consider Hashing or other approaches

Good luck! 🚀
"""

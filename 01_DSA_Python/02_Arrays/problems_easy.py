"""
================================================================
ARRAYS — EASY PROBLEMS (Start Here!)
================================================================
For each problem:
  1. Read the problem statement
  2. TRY to solve it yourself first (spend 10-15 min)
  3. Then read the approach explanation
  4. Then study the code
  5. Run the file to verify: python problems_easy.py
================================================================
"""


# ============================================================
# PROBLEM 1: Find the Largest Element in an Array
# ============================================================
"""
PROBLEM:
  Given a list of numbers, find the largest number.
  
  Input:  [3, 7, 2, 9, 1]
  Output: 9

WHY THIS PROBLEM?
  - Teaches basic traversal (going through each element)
  - This is the simplest array problem

APPROACH (Think step by step):
  1. Assume the first element is the largest
  2. Go through every other element
  3. If you find something bigger, update your answer
  4. After checking all elements, you have the largest

VISUAL:
  arr = [3, 7, 2, 9, 1]
  
  Start: max_val = 3 (first element)
  Check 7: 7 > 3? YES → max_val = 7
  Check 2: 2 > 7? NO  → max_val stays 7
  Check 9: 9 > 7? YES → max_val = 9
  Check 1: 1 > 9? NO  → max_val stays 9
  
  Answer: 9
"""

def find_largest(arr):
    if not arr:
        return None
    
    max_val = arr[0]          # Step 1: assume first is largest
    for i in range(1, len(arr)):  # Step 2: check rest
        if arr[i] > max_val:      # Step 3: found something bigger?
            max_val = arr[i]      # update
    return max_val                # Step 4: return answer

# TIME: O(n) — we look at each element once
# SPACE: O(1) — we only use one extra variable (max_val)

# Pythonic one-liner (know this too):
# def find_largest(arr): return max(arr)


# ============================================================
# PROBLEM 2: Find the Second Largest Element
# ============================================================
"""
PROBLEM:
  Given a list, find the second largest element.
  
  Input:  [3, 7, 2, 9, 1]
  Output: 7

  Input:  [5, 5, 5]
  Output: None (no second distinct largest)

APPROACH:
  1. Track both the largest and second largest
  2. One pass through the array
  3. If element > largest: second = largest, largest = element
  4. Elif element > second and element != largest: second = element

VISUAL:
  arr = [3, 7, 2, 9, 1]
  
  Start: first = -inf, second = -inf
  Check 3: 3 > -inf? YES → second = -inf, first = 3
  Check 7: 7 > 3?    YES → second = 3, first = 7
  Check 2: 2 > 7? NO. 2 > 3? NO → skip
           Wait, 2 > second(-inf)? NO, second is now 3. 2 > 3? NO → skip
  Check 9: 9 > 7?    YES → second = 7, first = 9
  Check 1: 1 > 9? NO. 1 > 7? NO → skip
  
  Answer: second = 7
"""

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')  # negative infinity
    
    for num in arr:
        if num > first:
            second = first    # old largest becomes second
            first = num       # new largest
        elif num > second and num != first:
            second = num      # new second largest
    
    return second if second != float('-inf') else None

# TIME: O(n) — single pass
# SPACE: O(1)


# ============================================================
# PROBLEM 3: Check if Array is Sorted
# ============================================================
"""
PROBLEM:
  Check if a given array is sorted in non-decreasing order.
  
  Input:  [1, 2, 3, 4, 5]  → True
  Input:  [1, 3, 2, 4, 5]  → False

APPROACH:
  Compare each element with the NEXT one.
  If any element is GREATER than the next → not sorted.

VISUAL:
  arr = [1, 3, 2, 4, 5]
  
  Compare 1 and 3: 1 <= 3 ✓
  Compare 3 and 2: 3 <= 2 ✗ → NOT SORTED!
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):    # go up to second-last element
        if arr[i] > arr[i + 1]:      # compare with next
            return False
    return True

# TIME: O(n)
# SPACE: O(1)


# ============================================================
# PROBLEM 4: Reverse an Array
# ============================================================
"""
PROBLEM:
  Reverse the array IN-PLACE (without creating a new array).
  
  Input:  [1, 2, 3, 4, 5]
  Output: [5, 4, 3, 2, 1]

APPROACH (Two Pointer Technique):
  Use two pointers: one at start, one at end.
  Swap them and move inward.

VISUAL:
  [1, 2, 3, 4, 5]
   ↑           ↑
   L           R     → swap 1 and 5 → [5, 2, 3, 4, 1]
   
  [5, 2, 3, 4, 1]
      ↑     ↑
      L     R        → swap 2 and 4 → [5, 4, 3, 2, 1]
   
  [5, 4, 3, 2, 1]
         ↑
        L=R          → L meets R, STOP!
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr  # modified in-place

# TIME: O(n) — we do n/2 swaps
# SPACE: O(1) — no extra array used!

# Pythonic alternatives (but know the manual way for interviews!):
# arr.reverse()     # in-place
# arr[::-1]         # creates new list


# ============================================================
# PROBLEM 5: Remove Duplicates from Sorted Array
# ============================================================
"""
PROBLEM (LeetCode 26):
  Given a SORTED array, remove duplicates IN-PLACE.
  Return the number of unique elements.
  
  Input:  [1, 1, 2, 2, 3, 4, 4]
  Output: 4 (array becomes [1, 2, 3, 4, ...])

WHY SORTED matters: All duplicates are NEXT TO each other!
  [1, 1, 2, 2, 3, 4, 4]
   ^  ^     ^  ^     ^   ← duplicates are adjacent

APPROACH (Two Pointer):
  - pointer 'i' tracks the position to write the next unique element
  - pointer 'j' scans through the array
  - When arr[j] != arr[i]: found new unique element → write it

VISUAL:
  arr = [1, 1, 2, 2, 3]
  i = 0, start scanning from j = 1
  
  j=1: arr[1]=1, arr[0]=1 → same, skip
  j=2: arr[2]=2, arr[0]=1 → DIFFERENT! i becomes 1, write arr[1]=2
  j=3: arr[3]=2, arr[1]=2 → same, skip
  j=4: arr[4]=3, arr[1]=2 → DIFFERENT! i becomes 2, write arr[2]=3
  
  Result: [1, 2, 3, ...], return i+1 = 3
"""

def remove_duplicates_sorted(arr):
    if not arr:
        return 0
    
    i = 0  # pointer for unique elements
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:      # found a new unique element
            i += 1                 # move unique pointer forward
            arr[i] = arr[j]       # place the unique element
    
    return i + 1  # number of unique elements

# TIME: O(n) — single pass
# SPACE: O(1) — in-place


# ============================================================
# PROBLEM 6: Move Zeros to End
# ============================================================
"""
PROBLEM (LeetCode 283):
  Move all zeros to the end while maintaining order of non-zero elements.
  Do it IN-PLACE.
  
  Input:  [0, 1, 0, 3, 12]
  Output: [1, 3, 12, 0, 0]

APPROACH:
  - Use pointer 'write_pos' to track where next non-zero should go
  - Scan through array, when you find non-zero, put it at write_pos
  - Fill remaining positions with zeros

VISUAL:
  arr = [0, 1, 0, 3, 12]
  write_pos = 0
  
  i=0: arr[0]=0  → skip (it's zero)
  i=1: arr[1]=1  → write arr[0]=1, write_pos=1
  i=2: arr[2]=0  → skip
  i=3: arr[3]=3  → write arr[1]=3, write_pos=2
  i=4: arr[4]=12 → write arr[2]=12, write_pos=3
  
  Now fill rest with zeros: arr[3]=0, arr[4]=0
  Result: [1, 3, 12, 0, 0] ✓
"""

def move_zeros(arr):
    write_pos = 0
    
    # Step 1: Move all non-zero elements to front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write_pos] = arr[i]
            write_pos += 1
    
    # Step 2: Fill remaining with zeros
    while write_pos < len(arr):
        arr[write_pos] = 0
        write_pos += 1
    
    return arr

# TIME: O(n)
# SPACE: O(1)


# ============================================================
# PROBLEM 7: Left Rotate Array by K positions
# ============================================================
"""
PROBLEM:
  Rotate array to the LEFT by K positions.
  
  Input:  arr = [1, 2, 3, 4, 5], k = 2
  Output: [3, 4, 5, 1, 2]
  
  Explanation:
    Rotate 1: [2, 3, 4, 5, 1]
    Rotate 2: [3, 4, 5, 1, 2]

APPROACH (Using Slicing — Easiest):
  After rotating left by k:
    - First k elements go to end
    - Remaining elements come to front
  
  arr[k:] + arr[:k]
  [3, 4, 5] + [1, 2] = [3, 4, 5, 1, 2]

IMPORTANT: Handle k >= len(arr) by using k = k % len(arr)
"""

def left_rotate(arr, k):
    if not arr:
        return arr
    
    k = k % len(arr)  # handle k larger than array length
    return arr[k:] + arr[:k]

# TIME: O(n) — slicing creates new lists
# SPACE: O(n) — new list created

# In-place approach (using reverse trick):
def left_rotate_inplace(arr, k):
    """
    Reverse trick:
    1. Reverse first k elements
    2. Reverse remaining elements
    3. Reverse entire array
    
    Example: [1, 2, 3, 4, 5], k=2
    Step 1: Reverse [1,2]     → [2, 1, 3, 4, 5]
    Step 2: Reverse [3,4,5]   → [2, 1, 5, 4, 3]
    Step 3: Reverse all       → [3, 4, 5, 1, 2] ✓
    """
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    n = len(arr)
    k = k % n
    
    reverse(arr, 0, k - 1)        # reverse first k
    reverse(arr, k, n - 1)        # reverse rest
    reverse(arr, 0, n - 1)        # reverse all
    
    return arr

# TIME: O(n), SPACE: O(1) — truly in-place!


# ============================================================
# PROBLEM 8: Find Missing Number
# ============================================================
"""
PROBLEM (LeetCode 268):
  Array contains n distinct numbers from 0, 1, 2, ..., n.
  Find the ONE missing number.
  
  Input:  [3, 0, 1]     → Output: 2 (numbers should be 0,1,2,3)
  Input:  [0, 1]        → Output: 2

APPROACH 1: Sum formula
  Sum of 0 to n = n * (n + 1) / 2
  Missing = expected_sum - actual_sum

VISUAL:
  arr = [3, 0, 1], n = 3
  Expected sum of 0..3 = 3 * 4 / 2 = 6
  Actual sum = 3 + 0 + 1 = 4
  Missing = 6 - 4 = 2 ✓
"""

def find_missing_number(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# TIME: O(n)
# SPACE: O(1)


# ============================================================
# PROBLEM 9: Find Single Number (all others appear twice)
# ============================================================
"""
PROBLEM (LeetCode 136):
  Every element appears TWICE except one. Find the single one.
  
  Input:  [4, 1, 2, 1, 2]  → Output: 4
  Input:  [2, 2, 1]        → Output: 1

APPROACH: XOR (^) Trick
  XOR properties:
    a ^ a = 0       (same numbers cancel out)
    a ^ 0 = a       (XOR with 0 gives same number)
    XOR is commutative and associative (order doesn't matter)
  
  So: 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4

If XOR is confusing, simpler approach: use a set or Counter.
"""

def single_number(arr):
    result = 0
    for num in arr:
        result ^= num  # XOR all elements
    return result

# TIME: O(n)
# SPACE: O(1)

# Simpler approach if XOR is confusing:
def single_number_simple(arr):
    from collections import Counter
    count = Counter(arr)
    for num, cnt in count.items():
        if cnt == 1:
            return num


# ============================================================
# PROBLEM 10: Two Sum (VERY IMPORTANT — Asked Everywhere!)
# ============================================================
"""
PROBLEM (LeetCode 1):
  Given an array and a target, find TWO numbers that add up to target.
  Return their INDICES.
  
  Input:  nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]  (because nums[0] + nums[1] = 2 + 7 = 9)

APPROACH 1: Brute Force — Check every pair
  For each element, check every OTHER element.
  Time: O(n²) — TOO SLOW for interviews

APPROACH 2: Hash Map (OPTIMAL)
  For each number, we need (target - number) to exist.
  Store numbers we've seen in a dictionary for O(1) lookup.

VISUAL (Approach 2):
  nums = [2, 7, 11, 15], target = 9
  seen = {}
  
  i=0: num=2, need=9-2=7, is 7 in seen? NO  → seen = {2: 0}
  i=1: num=7, need=9-7=2, is 2 in seen? YES → return [seen[2], 1] = [0, 1] ✓
"""

# Brute Force (KNOW this but tell interviewer it's not optimal)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
# TIME: O(n²), SPACE: O(1)

# Optimal (USE THIS in interviews)
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
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TESTING ALL EASY ARRAY PROBLEMS")
    print("=" * 60)
    
    # Problem 1: Find Largest
    print("\n--- Problem 1: Find Largest ---")
    print(f"[3, 7, 2, 9, 1] → {find_largest([3, 7, 2, 9, 1])}")  # 9
    print(f"[1] → {find_largest([1])}")  # 1
    print(f"[-5, -2, -8] → {find_largest([-5, -2, -8])}")  # -2
    
    # Problem 2: Second Largest
    print("\n--- Problem 2: Second Largest ---")
    print(f"[3, 7, 2, 9, 1] → {find_second_largest([3, 7, 2, 9, 1])}")  # 7
    print(f"[5, 5, 5] → {find_second_largest([5, 5, 5])}")  # None
    print(f"[10, 5] → {find_second_largest([10, 5])}")  # 5
    
    # Problem 3: Is Sorted
    print("\n--- Problem 3: Is Sorted ---")
    print(f"[1, 2, 3, 4, 5] → {is_sorted([1, 2, 3, 4, 5])}")  # True
    print(f"[1, 3, 2, 4, 5] → {is_sorted([1, 3, 2, 4, 5])}")  # False
    
    # Problem 4: Reverse Array
    print("\n--- Problem 4: Reverse Array ---")
    print(f"[1, 2, 3, 4, 5] → {reverse_array([1, 2, 3, 4, 5])}")  # [5,4,3,2,1]
    
    # Problem 5: Remove Duplicates from Sorted
    print("\n--- Problem 5: Remove Duplicates (Sorted) ---")
    arr = [1, 1, 2, 2, 3, 4, 4]
    k = remove_duplicates_sorted(arr)
    print(f"[1, 1, 2, 2, 3, 4, 4] → {k} unique, arr = {arr[:k]}")  # 4, [1,2,3,4]
    
    # Problem 6: Move Zeros
    print("\n--- Problem 6: Move Zeros ---")
    print(f"[0, 1, 0, 3, 12] → {move_zeros([0, 1, 0, 3, 12])}")  # [1,3,12,0,0]
    
    # Problem 7: Left Rotate
    print("\n--- Problem 7: Left Rotate ---")
    print(f"[1,2,3,4,5] k=2 → {left_rotate([1, 2, 3, 4, 5], 2)}")  # [3,4,5,1,2]
    print(f"In-place: {left_rotate_inplace([1, 2, 3, 4, 5], 2)}")  # [3,4,5,1,2]
    
    # Problem 8: Missing Number
    print("\n--- Problem 8: Missing Number ---")
    print(f"[3, 0, 1] → {find_missing_number([3, 0, 1])}")  # 2
    print(f"[0, 1] → {find_missing_number([0, 1])}")  # 2
    
    # Problem 9: Single Number
    print("\n--- Problem 9: Single Number ---")
    print(f"[4, 1, 2, 1, 2] → {single_number([4, 1, 2, 1, 2])}")  # 4
    print(f"[2, 2, 1] → {single_number([2, 2, 1])}")  # 1
    
    # Problem 10: Two Sum
    print("\n--- Problem 10: Two Sum ---")
    print(f"[2, 7, 11, 15] target=9 → {two_sum([2, 7, 11, 15], 9)}")  # [0, 1]
    print(f"[3, 2, 4] target=6 → {two_sum([3, 2, 4], 6)}")  # [1, 2]
    
    print("\n✅ All easy problems done! Move to problems_medium.py")

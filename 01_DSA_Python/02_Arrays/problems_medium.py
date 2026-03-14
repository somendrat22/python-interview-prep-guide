"""
================================================================
ARRAYS — MEDIUM PROBLEMS (Interview Level)
================================================================
These are the type of problems asked in JP Morgan SDE2 interviews.
Make sure you can solve Easy problems comfortably before attempting these.
================================================================
"""


# ============================================================
# PROBLEM 1: Best Time to Buy and Sell Stock (LeetCode 121)
# ============================================================
"""
PROBLEM:
  You have an array where prices[i] is the stock price on day i.
  You can buy on ONE day and sell on a LATER day.
  Find the MAXIMUM profit. If no profit possible, return 0.
  
  Input:  [7, 1, 5, 3, 6, 4]
  Output: 5  (Buy on day 1 at price 1, sell on day 4 at price 6 → 6-1=5)

  Input:  [7, 6, 4, 3, 1]
  Output: 0  (prices only decrease, no profit possible)

WHY THIS IS IMPORTANT:
  - Asked in almost EVERY company
  - Tests your understanding of tracking minimum and maximum

APPROACH:
  - Track the MINIMUM price seen so far (best day to buy)
  - At each day, calculate profit if we sell today
  - Track the MAXIMUM profit seen

VISUAL:
  prices = [7, 1, 5, 3, 6, 4]
  
  Day 0: price=7, min_price=7, profit=7-7=0, max_profit=0
  Day 1: price=1, min_price=1, profit=1-1=0, max_profit=0
  Day 2: price=5, min_price=1, profit=5-1=4, max_profit=4
  Day 3: price=3, min_price=1, profit=3-1=2, max_profit=4
  Day 4: price=6, min_price=1, profit=6-1=5, max_profit=5 ✓
  Day 5: price=4, min_price=1, profit=4-1=3, max_profit=5
  
  Answer: 5
"""

def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]   # cheapest price seen so far
    max_profit_val = 0      # best profit seen so far
    
    for i in range(1, len(prices)):
        # Could we get a better profit by selling today?
        profit_today = prices[i] - min_price
        max_profit_val = max(max_profit_val, profit_today)
        
        # Update the cheapest buying price
        min_price = min(min_price, prices[i])
    
    return max_profit_val

# TIME: O(n) — single pass
# SPACE: O(1)


# ============================================================
# PROBLEM 2: Container With Most Water (LeetCode 11)
# ============================================================
"""
PROBLEM:
  Given array 'height' where height[i] is the height of a vertical line
  at position i. Find two lines that together with the x-axis form a
  container that holds the MOST water.
  
  Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Output: 49

  The container is formed by height[1]=8 and height[8]=7
  Width = 8 - 1 = 7
  Height = min(8, 7) = 7  (water level = shorter line)
  Area = 7 * 7 = 49

APPROACH: Two Pointers
  - Start with widest container (left=0, right=end)
  - Calculate area
  - Move the SHORTER pointer inward (because moving the taller one
    can never increase the height, and width is decreasing)

VISUAL:
  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  
  L=0, R=8: area = min(1,7) * 8 = 8.   Move L (1 < 7)
  L=1, R=8: area = min(8,7) * 7 = 49.  Move R (7 < 8)
  L=1, R=7: area = min(8,3) * 6 = 18.  Move R (3 < 8)
  ... continue ...
  
  Max area found: 49
"""

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Width = distance between the two lines
        width = right - left
        # Height = the shorter of the two lines
        h = min(height[left], height[right])
        # Area = width * height
        area = width * h
        max_water = max(max_water, area)
        
        # Move the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# TIME: O(n) — each pointer moves at most n times
# SPACE: O(1)


# ============================================================
# PROBLEM 3: Maximum Subarray Sum (Kadane's Algorithm) (LeetCode 53)
# ============================================================
"""
PROBLEM:
  Find the contiguous subarray with the LARGEST sum.
  
  Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  Output: 6  (subarray [4, -1, 2, 1] has sum 6)

WHY THIS IS IMPORTANT:
  - Classic DP/greedy problem
  - Kadane's Algorithm is asked VERY frequently
  - Must know this by heart

APPROACH (Kadane's Algorithm):
  At each position, decide:
    - Should I EXTEND the previous subarray (add current element)?
    - Or should I START a new subarray from current element?
  
  Decision: current_sum = max(num, current_sum + num)
    If current_sum + num < num, that means current_sum was NEGATIVE,
    so it's better to start fresh.

VISUAL:
  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  
  i=0: num=-2, current=max(-2, 0+(-2))=-2, max_sum=-2
  i=1: num= 1, current=max(1, -2+1)=max(1,-1)=1, max_sum=1
  i=2: num=-3, current=max(-3, 1+(-3))=max(-3,-2)=-2, max_sum=1
  i=3: num= 4, current=max(4, -2+4)=max(4,2)=4, max_sum=4
  i=4: num=-1, current=max(-1, 4+(-1))=max(-1,3)=3, max_sum=4
  i=5: num= 2, current=max(2, 3+2)=max(2,5)=5, max_sum=5
  i=6: num= 1, current=max(1, 5+1)=max(1,6)=6, max_sum=6 ✓
  i=7: num=-5, current=max(-5, 6+(-5))=max(-5,1)=1, max_sum=6
  i=8: num= 4, current=max(4, 1+4)=max(4,5)=5, max_sum=6
  
  Answer: 6
"""

def max_subarray_sum(arr):
    if not arr:
        return 0
    
    current_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend previous subarray or start new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# TIME: O(n) — single pass
# SPACE: O(1)


# ============================================================
# PROBLEM 4: Product of Array Except Self (LeetCode 238)
# ============================================================
"""
PROBLEM:
  Return an array where result[i] = product of all elements EXCEPT nums[i].
  Do NOT use division.
  
  Input:  [1, 2, 3, 4]
  Output: [24, 12, 8, 6]
  
  result[0] = 2*3*4 = 24
  result[1] = 1*3*4 = 12
  result[2] = 1*2*4 = 8
  result[3] = 1*2*3 = 6

APPROACH:
  For each position i, the answer = (product of everything LEFT of i)
                                    * (product of everything RIGHT of i)
  
  Step 1: Calculate LEFT products (prefix products)
  Step 2: Calculate RIGHT products (suffix products)
  Step 3: Multiply them

VISUAL:
  nums =    [1,  2,  3,  4]
  
  Left products (what's to my left):
  left =    [1,  1,  2,  6]
             ↑   ↑   ↑   ↑
            nothing 1  1*2 1*2*3
  
  Right products (what's to my right):
  right =   [24, 12, 4,  1]
              ↑   ↑   ↑   ↑
            2*3*4 3*4  4  nothing
  
  Answer = left[i] * right[i]:
  result =  [24, 12, 8,  6] ✓
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Step 1: Fill result with LEFT products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Step 2: Multiply with RIGHT products
    right_product = 1
    for i in range(n - 1, -1, -1):  # go right to left
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# TIME: O(n) — two passes
# SPACE: O(1) — result array doesn't count as extra space per problem statement


# ============================================================
# PROBLEM 5: Sort Colors / Dutch National Flag (LeetCode 75)
# ============================================================
"""
PROBLEM:
  Array contains only 0s, 1s, and 2s. Sort IN-PLACE in one pass.
  
  Input:  [2, 0, 2, 1, 1, 0]
  Output: [0, 0, 1, 1, 2, 2]

APPROACH (Dutch National Flag — 3 Pointers):
  - low pointer: everything before low is 0
  - mid pointer: current element being examined
  - high pointer: everything after high is 2
  
  Rules:
    If arr[mid] == 0: swap with low, move both low and mid forward
    If arr[mid] == 1: just move mid forward (1s stay in middle)
    If arr[mid] == 2: swap with high, move high backward (DON'T move mid!)

VISUAL:
  arr = [2, 0, 2, 1, 1, 0]
  low=0, mid=0, high=5
  
  mid=0: arr[0]=2 → swap with high → [0, 0, 2, 1, 1, 2], high=4
  mid=0: arr[0]=0 → swap with low  → [0, 0, 2, 1, 1, 2], low=1, mid=1
  mid=1: arr[1]=0 → swap with low  → [0, 0, 2, 1, 1, 2], low=2, mid=2
  mid=2: arr[2]=2 → swap with high → [0, 0, 1, 1, 2, 2], high=3
  mid=2: arr[2]=1 → mid=3
  mid=3: arr[3]=1 → mid=4
  mid=4 > high=3 → STOP
  
  Result: [0, 0, 1, 1, 2, 2] ✓
"""

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # DON'T increment mid! We need to check swapped element
    
    return nums

# TIME: O(n) — single pass
# SPACE: O(1)


# ============================================================
# PROBLEM 6: Merge Two Sorted Arrays (LeetCode 88)
# ============================================================
"""
PROBLEM:
  Given two sorted arrays nums1 and nums2, merge nums2 INTO nums1.
  nums1 has enough space (zeros at end) to hold both arrays.
  
  Input:  nums1 = [1, 2, 3, 0, 0, 0], m = 3
          nums2 = [2, 5, 6],           n = 3
  Output: [1, 2, 2, 3, 5, 6]

APPROACH: Fill from the END (avoids overwriting)
  - Use three pointers: p1 at end of nums1's data, p2 at end of nums2,
    write_pos at end of nums1's total space
  - Compare from the back, place the LARGER element at write_pos

VISUAL:
  nums1 = [1, 2, 3, 0, 0, 0], nums2 = [2, 5, 6]
                 ↑                          ↑     ↑
                p1                         p2   write
  
  Compare 3 vs 6: 6 > 3 → place 6 at end → [1, 2, 3, 0, 0, 6]
  Compare 3 vs 5: 5 > 3 → place 5         → [1, 2, 3, 0, 5, 6]
  Compare 3 vs 2: 3 > 2 → place 3         → [1, 2, 3, 3, 5, 6]
                                              wait, we overwrite but p1 moved left
  Actually: → [1, 2, _, 3, 5, 6] then [1, 2, 2, 3, 5, 6]
  
  Result: [1, 2, 2, 3, 5, 6] ✓
"""

def merge_sorted(nums1, m, nums2, n):
    p1 = m - 1           # pointer at end of nums1's actual data
    p2 = n - 1           # pointer at end of nums2
    write = m + n - 1    # pointer at end of nums1's total space
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1
    
    # If nums2 has remaining elements, copy them
    while p2 >= 0:
        nums1[write] = nums2[p2]
        p2 -= 1
        write -= 1
    
    # No need to copy remaining nums1 — they're already in place!
    return nums1

# TIME: O(m + n)
# SPACE: O(1)


# ============================================================
# PROBLEM 7: Spiral Matrix (LeetCode 54)
# ============================================================
"""
PROBLEM:
  Given an m x n matrix, return all elements in spiral order.
  
  Input:  [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
  Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

  Spiral: → right along top, ↓ down right side, ← left along bottom, ↑ up left side
  
  1 → 2 → 3
              ↓
  4 → 5   6
  ↑       ↓
  7 ← 8 ← 9

APPROACH: Shrinking Boundaries
  Maintain four boundaries: top, bottom, left, right
  After traversing each direction, shrink that boundary.
"""

def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # → Traverse top row (left to right)
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # ↓ Traverse right column (top to bottom)
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # ← Traverse bottom row (right to left)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # ↑ Traverse left column (bottom to top)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# TIME: O(m * n) — visit every element once
# SPACE: O(1) — not counting output array


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TESTING ALL MEDIUM ARRAY PROBLEMS")
    print("=" * 60)
    
    # Problem 1
    print("\n--- Problem 1: Best Time to Buy/Sell Stock ---")
    print(f"[7,1,5,3,6,4] → {max_profit([7,1,5,3,6,4])}")    # 5
    print(f"[7,6,4,3,1] → {max_profit([7,6,4,3,1])}")         # 0
    
    # Problem 2
    print("\n--- Problem 2: Container With Most Water ---")
    print(f"[1,8,6,2,5,4,8,3,7] → {max_area([1,8,6,2,5,4,8,3,7])}")  # 49
    
    # Problem 3
    print("\n--- Problem 3: Maximum Subarray (Kadane's) ---")
    print(f"[-2,1,-3,4,-1,2,1,-5,4] → {max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])}")  # 6
    print(f"[1] → {max_subarray_sum([1])}")  # 1
    print(f"[-1] → {max_subarray_sum([-1])}")  # -1
    
    # Problem 4
    print("\n--- Problem 4: Product Except Self ---")
    print(f"[1,2,3,4] → {product_except_self([1,2,3,4])}")    # [24,12,8,6]
    print(f"[-1,1,0,-3,3] → {product_except_self([-1,1,0,-3,3])}")  # [0,0,9,0,0]
    
    # Problem 5
    print("\n--- Problem 5: Sort Colors ---")
    print(f"[2,0,2,1,1,0] → {sort_colors([2,0,2,1,1,0])}")   # [0,0,1,1,2,2]
    print(f"[2,0,1] → {sort_colors([2,0,1])}")                 # [0,1,2]
    
    # Problem 6
    print("\n--- Problem 6: Merge Sorted Arrays ---")
    nums1 = [1,2,3,0,0,0]
    print(f"merge → {merge_sorted(nums1, 3, [2,5,6], 3)}")    # [1,2,2,3,5,6]
    
    # Problem 7
    print("\n--- Problem 7: Spiral Matrix ---")
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(f"3x3 spiral → {spiral_order(matrix)}")  # [1,2,3,6,9,8,7,4,5]
    
    print("\n✅ All medium problems done! Great job!")

"""
================================================================
TOPIC 12: SORTING & SEARCHING - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHY LEARN SORTING?
================================================================

Sorting = arranging elements in a specific order (ascending/descending).

Why is it important?
  - Many problems become EASY once data is sorted
  - Binary search requires sorted data
  - Interviewers test if you understand O(n log n) vs O(n^2)
  - Python's built-in sort (Timsort) is O(n log n) - know when to use it!

SORTING ALGORITHMS COMPARISON:
  
  Algorithm        | Best    | Average  | Worst   | Space | Stable?
  -----------------|---------|----------|---------|-------|--------
  Bubble Sort      | O(n)    | O(n^2)   | O(n^2)  | O(1)  | Yes
  Selection Sort   | O(n^2)  | O(n^2)   | O(n^2)  | O(1)  | No
  Insertion Sort   | O(n)    | O(n^2)   | O(n^2)  | O(1)  | Yes
  Merge Sort       | O(nlogn)| O(nlogn) | O(nlogn)| O(n)  | Yes
  Quick Sort       | O(nlogn)| O(nlogn) | O(n^2)  | O(logn)| No
  Python sorted()  | O(nlogn)| O(nlogn) | O(nlogn)| O(n)  | Yes

  Stable = Equal elements maintain their relative order.

FOR INTERVIEWS: Know Merge Sort and Quick Sort well.
  - Merge Sort: predictable O(n log n), uses extra space
  - Quick Sort: usually fastest in practice, but O(n^2) worst case


================================================================
SECTION 2: BASIC SORTING ALGORITHMS (Understand the concepts)
================================================================
"""


# ============================================================
# BUBBLE SORT - Simplest to understand
# ============================================================
"""
IDEA: Repeatedly swap adjacent elements if they're in wrong order.
Each pass "bubbles" the largest unsorted element to its correct position.

VISUAL:
  [5, 3, 8, 1, 2]
  
  Pass 1: Compare adjacent pairs, swap if needed
    5,3 -> swap -> [3, 5, 8, 1, 2]
    5,8 -> ok   -> [3, 5, 8, 1, 2]
    8,1 -> swap -> [3, 5, 1, 8, 2]
    8,2 -> swap -> [3, 5, 1, 2, 8]  <- 8 is in place!
  
  Pass 2: [3, 1, 2, 5, 8] <- 5 is in place
  Pass 3: [1, 2, 3, 5, 8] <- sorted!
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # optimization: already sorted
            break
    return arr

# TIME: O(n^2) average/worst, O(n) best (already sorted)
# SPACE: O(1)


# ============================================================
# INSERTION SORT - Good for small/nearly sorted arrays
# ============================================================
"""
IDEA: Build sorted array one element at a time.
Take each element and INSERT it into its correct position in the sorted part.

Like sorting playing cards in your hand:
  Pick up each card and insert it in the right spot.

VISUAL:
  [5, 3, 8, 1, 2]
   ^sorted
  
  Insert 3: [3, 5, 8, 1, 2]    (3 < 5, insert before 5)
  Insert 8: [3, 5, 8, 1, 2]    (8 > 5, stays)
  Insert 1: [1, 3, 5, 8, 2]    (1 < 3, insert at beginning)
  Insert 2: [1, 2, 3, 5, 8]    (2 > 1 and < 3, insert there)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# TIME: O(n^2) average/worst, O(n) best
# SPACE: O(1)


# ============================================================
# MERGE SORT - Important! O(n log n) guaranteed
# ============================================================
"""
IDEA: Divide and Conquer
  1. DIVIDE array into two halves
  2. SORT each half recursively
  3. MERGE the two sorted halves

VISUAL:
  [5, 3, 8, 1, 2, 7, 4, 6]
  
  Split: [5, 3, 8, 1] | [2, 7, 4, 6]
  Split: [5, 3] [8, 1] | [2, 7] [4, 6]
  Split: [5] [3] [8] [1] | [2] [7] [4] [6]
  
  Merge: [3, 5] [1, 8] | [2, 7] [4, 6]
  Merge: [1, 3, 5, 8] | [2, 4, 6, 7]
  Merge: [1, 2, 3, 4, 5, 6, 7, 8]
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# TIME: O(n log n) always
# SPACE: O(n) for the merged arrays


# ============================================================
# QUICK SORT - Usually fastest in practice
# ============================================================
"""
IDEA: Divide and Conquer with PIVOT
  1. Pick a PIVOT element
  2. PARTITION: put smaller elements left, larger elements right
  3. Recursively sort left and right parts

VISUAL (pivot = last element):
  [5, 3, 8, 1, 2, 7, 4, 6]   pivot = 6
  
  Partition around 6:
  [5, 3, 1, 2, 4] [6] [8, 7]
  
  Recursively sort left and right parts.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # choose last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# TIME: O(n log n) average, O(n^2) worst (already sorted + bad pivot)
# SPACE: O(n) for this implementation


"""
================================================================
SECTION 3: BINARY SEARCH - The Most Important Search Algorithm!
================================================================

Binary Search works on SORTED arrays.
Instead of checking every element O(n), it eliminates HALF
the remaining elements each step -> O(log n).

VISUAL:
  Find 23 in: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
  
  Step 1: mid = 16. 23 > 16 -> search RIGHT half
           [23, 38, 56, 72, 91]
  
  Step 2: mid = 56. 23 < 56 -> search LEFT half
           [23, 38]
  
  Step 3: mid = 23. FOUND!
  
  Only 3 steps instead of 6 (linear search)!
  For 1 billion elements: only ~30 steps!
"""

def binary_search(arr, target):
    """
    Find target in sorted array. Return index or -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # target is in right half
        else:
            right = mid - 1     # target is in left half
    
    return -1  # not found

# TIME: O(log n), SPACE: O(1)


# ============================================================
# BINARY SEARCH VARIATIONS
# ============================================================

def find_first_occurrence(arr, target):
    """Find the FIRST (leftmost) occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # keep searching LEFT for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr, target):
    """Find the LAST (rightmost) occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1   # keep searching RIGHT for later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def search_rotated_array(nums, target):
    """
    LeetCode 33: Search in Rotated Sorted Array.
    [4, 5, 6, 7, 0, 1, 2] was originally sorted then rotated.
    Find target in O(log n).
    
    KEY INSIGHT: One half is ALWAYS sorted.
    Determine which half is sorted, check if target is in that half.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # target in left sorted half
            else:
                left = mid + 1    # target in right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # target in right sorted half
            else:
                right = mid - 1   # target in left half
    
    return -1


def find_peak_element(nums):
    """
    LeetCode 162: Find a peak element (greater than neighbors).
    Binary search on the slope direction.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1    # peak is to the right
        else:
            right = mid       # peak is here or to the left
    
    return left


def find_sqrt(x):
    """
    LeetCode 69: Integer square root.
    Find largest n where n*n <= x.
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # right is the floor of sqrt


"""
================================================================
SUMMARY
================================================================

SORTING:
  - For interviews: know Merge Sort and Quick Sort
  - In practice: use Python's sorted() / .sort() (Timsort)
  - Bubble/Insertion: understand concept, O(n^2)
  - Merge Sort: O(n log n) guaranteed, O(n) space, stable
  - Quick Sort: O(n log n) average, O(1) extra space, not stable

BINARY SEARCH:
  - ONLY works on sorted data
  - O(log n) time
  - Template: left, right, while left <= right, mid = (left+right)//2
  - Variations: first/last occurrence, rotated array, peak finding
  
WHEN TO USE BINARY SEARCH:
  - "Find element in sorted array"
  - "Find minimum/maximum that satisfies a condition"
  - "Search in rotated sorted array"
  - Any problem where you can eliminate half the search space
"""


if __name__ == "__main__":
    print("=" * 60)
    print("SORTING & SEARCHING EXAMPLES")
    print("=" * 60)
    
    arr = [5, 3, 8, 1, 2, 7, 4, 6]
    
    print(f"\nOriginal: {arr}")
    print(f"Bubble Sort:    {bubble_sort(arr[:])}")
    print(f"Insertion Sort: {insertion_sort(arr[:])}")
    print(f"Merge Sort:     {merge_sort(arr[:])}")
    print(f"Quick Sort:     {quick_sort(arr[:])}")
    print(f"Python sorted:  {sorted(arr)}")
    
    print(f"\n--- Binary Search ---")
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Array: {sorted_arr}")
    print(f"Find 23: index = {binary_search(sorted_arr, 23)}")
    print(f"Find 99: index = {binary_search(sorted_arr, 99)}")
    
    print(f"\n--- First/Last Occurrence ---")
    arr2 = [1, 2, 2, 2, 3, 4, 5]
    print(f"Array: {arr2}")
    print(f"First 2: index = {find_first_occurrence(arr2, 2)}")  # 1
    print(f"Last 2:  index = {find_last_occurrence(arr2, 2)}")   # 3
    
    print(f"\n--- Search Rotated Array ---")
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"Array: {rotated}")
    print(f"Find 0: index = {search_rotated_array(rotated, 0)}")  # 4
    
    print(f"\n--- Square Root ---")
    print(f"sqrt(8) = {find_sqrt(8)}")    # 2
    print(f"sqrt(16) = {find_sqrt(16)}")  # 4
    
    print("\nDone! Sorting & Searching complete!")


# ============================================================
# QUESTION APPROACH GUIDE — DETAILED EXPLANATIONS
# ============================================================
"""
================================================================
HOW TO IDENTIFY SORTING/SEARCHING PROBLEMS
================================================================

USE SORTING WHEN:
  ✓ "Find pairs/triplets with sum"
  ✓ "Merge intervals"
  ✓ "Meeting rooms"
  ✓ "Kth largest/smallest element"
  ✓ Order doesn't matter in input

USE BINARY SEARCH WHEN:
  ✓ Array is SORTED
  ✓ "Find element in O(log n)"
  ✓ "Find first/last occurrence"
  ✓ "Search in rotated array"
  ✓ "Find minimum/maximum that satisfies condition"
  ✓ Can eliminate half the search space


================================================================
DETAILED PROBLEM-SOLVING APPROACHES
================================================================
"""


# --- APPROACH 1: Merge Intervals ---
def merge_intervals_detailed(intervals):
    """
    PROBLEM: Merge overlapping intervals.
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    
    WHY SORTING?
    - Overlapping intervals must be adjacent after sorting
    - Sort by start time
    - Then merge consecutive overlapping intervals
    
    APPROACH:
    1. Sort intervals by start time
    2. Iterate through sorted intervals
    3. If current overlaps with last merged:
       - Extend the last merged interval
    4. Otherwise:
       - Add current as new interval
    
    VISUALIZATION:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    
    After sort: [[1,3],[2,6],[8,10],[15,18]]
    
    Process:
    [1,3] → merged = [[1,3]]
    [2,6] → overlaps with [1,3] (2 <= 3) → extend to [1,6]
            merged = [[1,6]]
    [8,10] → no overlap (8 > 6) → add new
             merged = [[1,6],[8,10]]
    [15,18] → no overlap (15 > 10) → add new
              merged = [[1,6],[8,10],[15,18]]
    
    OVERLAP CONDITION:
    - current.start <= last.end
    
    TIME: O(n log n) for sorting, SPACE: O(n)
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if overlapping
        if current[0] <= last[1]:
            # Merge by extending end time
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged


# --- APPROACH 2: Binary Search Variations ---
def binary_search_detailed(arr, target):
    """
    PROBLEM: Find target in sorted array.
    
    WHY BINARY SEARCH?
    - Array is SORTED
    - Can eliminate half the search space each step
    - O(log n) vs O(n) linear search
    
    KEY INSIGHT:
    - Compare target with middle element
    - If target < mid: search left half
    - If target > mid: search right half
    - If target == mid: found!
    
    TEMPLATE (MUST MEMORIZE):
    ```
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
    ```
    
    COMMON VARIATIONS:
    1. Find first occurrence
    2. Find last occurrence
    3. Find insertion position
    4. Search in rotated array
    
    TIME: O(log n), SPACE: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_first_occurrence_detailed(arr, target):
    """
    PROBLEM: Find FIRST (leftmost) occurrence of target.
    Input: [1,2,2,2,3], target=2
    Output: 1
    
    WHY DIFFERENT FROM REGULAR BINARY SEARCH?
    - When we find target, there might be more to the left
    - Continue searching left half
    
    MODIFICATION:
    - When arr[mid] == target:
      → Don't return immediately
      → Save result and search left: right = mid - 1
    
    VISUALIZATION:
    arr = [1,2,2,2,3], target=2
    
    left=0, right=4, mid=2: arr[2]=2 → found! result=2, search left
    left=0, right=1, mid=0: arr[0]=1 < 2 → search right
    left=1, right=1, mid=1: arr[1]=2 → found! result=1, search left
    left=1, right=0 → stop
    
    Return result=1 ✓
    
    TIME: O(log n), SPACE: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# --- APPROACH 3: Search in Rotated Sorted Array ---
def search_rotated_detailed(nums, target):
    """
    PROBLEM: Search in rotated sorted array.
    Input: [4,5,6,7,0,1,2], target=0
    Output: 4
    
    WHY BINARY SEARCH STILL WORKS?
    - One half is ALWAYS sorted
    - Determine which half is sorted
    - Check if target is in sorted half
    - If yes, search there; if no, search other half
    
    KEY INSIGHT:
    - If nums[left] <= nums[mid]: left half is sorted
    - Otherwise: right half is sorted
    
    VISUALIZATION:
    arr = [4,5,6,7,0,1,2], target=0
    
    left=0, right=6, mid=3: arr[3]=7
    - nums[0]=4 <= nums[3]=7 → left half [4,5,6,7] is sorted
    - Is 0 in [4,7]? No
    - Search right half
    
    left=4, right=6, mid=5: arr[5]=1
    - nums[4]=0 > nums[5]=1 → right half [1,2] is sorted
    - Is 0 in [1,2]? No
    - Search left half
    
    left=4, right=4, mid=4: arr[4]=0
    - Found! Return 4
    
    TIME: O(log n), SPACE: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left sorted half
            else:
                left = mid + 1   # Target in right half
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right sorted half
            else:
                right = mid - 1  # Target in left half
    
    return -1


# --- APPROACH 4: Kth Largest Element ---
def find_kth_largest_detailed(nums, k):
    """
    PROBLEM: Find kth largest element.
    Input: [3,2,1,5,6,4], k=2
    Output: 5
    
    APPROACH 1: Sorting
    - Sort array in descending order
    - Return element at index k-1
    TIME: O(n log n), SPACE: O(1) if in-place
    
    APPROACH 2: Min Heap of size k
    - Maintain min heap of k largest elements
    - Top of heap is kth largest
    TIME: O(n log k), SPACE: O(k)
    
    APPROACH 3: QuickSelect (Optimal)
    - Like QuickSort but only recurse on one side
    - Average O(n), Worst O(n²)
    
    FOR INTERVIEWS: Use heap or sorting (simpler)
    """
    import heapq
    
    # Method 1: Sorting (simplest)
    nums.sort(reverse=True)
    return nums[k-1]
    
    # Method 2: Min heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
    
    # Method 3: Using heapq.nlargest (cleanest)
    return heapq.nlargest(k, nums)[-1]


# --- APPROACH 5: Meeting Rooms II ---
def min_meeting_rooms_detailed(intervals):
    """
    PROBLEM: Find minimum number of meeting rooms needed.
    Input: [[0,30],[5,10],[15,20]]
    Output: 2
    
    WHY SORTING?
    - Need to know when meetings start and end
    - Sort start times and end times separately
    - Use two pointers to track overlaps
    
    APPROACH:
    1. Separate start and end times
    2. Sort both
    3. Use two pointers:
       - If start < end: need new room (overlap)
       - If start >= end: can reuse room (meeting ended)
    
    VISUALIZATION:
    intervals = [[0,30],[5,10],[15,20]]
    
    starts = [0, 5, 15]
    ends   = [10, 20, 30]
    
    s=0, e=0: start[0]=0 < end[0]=10 → need room, rooms=1
    s=1, e=0: start[1]=5 < end[0]=10 → need room, rooms=2
    s=2, e=0: start[2]=15 >= end[0]=10 → reuse room, e++
    s=2, e=1: start[2]=15 < end[1]=20 → (already counted)
    
    Max rooms needed: 2
    
    TIME: O(n log n), SPACE: O(n)
    """
    if not intervals:
        return 0
    
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = 0
    max_rooms = 0
    s = e = 0
    
    while s < len(starts):
        if starts[s] < ends[e]:
            # Need new room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            # Can reuse room
            rooms -= 1
            e += 1
    
    return max_rooms


# --- APPROACH 6: Find Peak Element ---
def find_peak_detailed(nums):
    """
    PROBLEM: Find a peak element (greater than neighbors).
    Input: [1,2,3,1]
    Output: 2 (index, value is 3)
    
    WHY BINARY SEARCH?
    - Don't need to check every element
    - Can use slope direction to guide search
    
    KEY INSIGHT:
    - If nums[mid] < nums[mid+1]: peak is to the right
    - Otherwise: peak is at mid or to the left
    
    VISUALIZATION:
    arr = [1,2,3,1]
    
    left=0, right=3, mid=1: nums[1]=2 < nums[2]=3
    - Slope going up → peak to the right
    - left = mid + 1 = 2
    
    left=2, right=3, mid=2: nums[2]=3 > nums[3]=1
    - Slope going down → peak at mid or left
    - right = mid = 2
    
    left=2, right=2 → stop, return 2
    
    TIME: O(log n), SPACE: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            # Peak is to the right
            left = mid + 1
        else:
            # Peak is at mid or to the left
            right = mid
    
    return left


"""
================================================================
COMMON MISTAKES TO AVOID
================================================================

❌ Wrong binary search bounds:
   while left < right:  # vs while left <= right:
   - Use <= for finding exact element
   - Use < for finding position/range

❌ Integer overflow in mid calculation:
   mid = (left + right) // 2  # Can overflow in other languages
   
   ✓ Use:
   mid = left + (right - left) // 2

❌ Infinite loop in binary search:
   - Make sure left and right always change
   - left = mid + 1 (not left = mid)
   - right = mid - 1 (not right = mid)

❌ Not sorting when needed:
   - Three sum, merge intervals need sorting first
   - Check if problem allows modifying input

❌ Forgetting edge cases:
   - Empty array
   - Single element
   - All same elements
   - Already sorted vs reverse sorted

❌ Using wrong sorting algorithm:
   - For interviews: use Python's sorted() or .sort()
   - Don't implement bubble sort unless asked


================================================================
INTERVIEW TIPS
================================================================

1. IDENTIFY IF SORTING HELPS
   "If we sort first, we can use two pointers..."
   "Sorting would group similar elements together..."
   "After sorting, overlapping intervals are adjacent..."

2. RECOGNIZE BINARY SEARCH OPPORTUNITIES
   "The array is sorted, so binary search..."
   "We can eliminate half the search space..."
   "This is a search problem with O(log n) hint..."

3. EXPLAIN YOUR APPROACH
   "I'll sort by start time, then merge overlapping intervals..."
   "Binary search because we can determine which half to search..."
   "We need O(n log n) for sorting, can't do better..."

4. DISCUSS COMPLEXITY
   "Sorting is O(n log n), then O(n) to merge..."
   "Binary search is O(log n) per query..."
   "We could use heap for O(n log k)..."

5. MENTION ALTERNATIVES
   "We could use QuickSelect for O(n) average..."
   "Heap would be O(n log k) instead of O(n log n)..."
   "If array is already sorted, we can skip sorting..."


================================================================
BINARY SEARCH TEMPLATE (MEMORIZE THIS!)
================================================================

# Standard Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Find First Occurrence
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Find Last Occurrence
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


================================================================
QUICK REFERENCE
================================================================

WHEN TO SORT:
  → Pairs/triplets with sum
  → Merge intervals
  → Meeting rooms
  → Kth largest (or use heap)

WHEN TO USE BINARY SEARCH:
  → Array is sorted
  → Find element in O(log n)
  → Find first/last occurrence
  → Search in rotated array
  → Find peak element

SORTING ALGORITHMS TO KNOW:
  → Merge Sort: O(n log n) always, stable
  → Quick Sort: O(n log n) average, not stable
  → Python sorted(): O(n log n), stable (Timsort)

BINARY SEARCH VARIATIONS:
  → Standard: find exact element
  → First occurrence: continue left when found
  → Last occurrence: continue right when found
  → Rotated array: check which half is sorted
  → Peak element: follow the slope

Good luck! 🚀
"""

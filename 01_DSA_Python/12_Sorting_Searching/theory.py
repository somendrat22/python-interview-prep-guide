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

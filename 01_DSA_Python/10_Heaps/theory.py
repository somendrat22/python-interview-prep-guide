"""
================================================================
TOPIC 10: HEAPS & PRIORITY QUEUES - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A HEAP?
================================================================

A Heap is a special BINARY TREE that satisfies the HEAP PROPERTY:
  - MIN HEAP: Parent is SMALLER than or equal to children
    (Root is the SMALLEST element)
  - MAX HEAP: Parent is LARGER than or equal to children
    (Root is the LARGEST element)

MIN HEAP example:
           1           <-- smallest on top!
          / \
         3   5
        / \ / \
       7  4 8  6

MAX HEAP example:
           9           <-- largest on top!
          / \
         7   8
        / \
       3   5

WHY USE A HEAP?
  - Get min/max element instantly: O(1)
  - Insert element: O(log n)
  - Remove min/max: O(log n)
  - Perfect for: "Find top K elements", "Kth largest/smallest"


================================================================
SECTION 2: HEAPS IN PYTHON - heapq module
================================================================

Python's heapq module implements a MIN HEAP.
The heap is stored as a regular list!

IMPORTANT: Python only has MIN HEAP built-in.
For MAX HEAP: negate values (multiply by -1).
"""

import heapq

# ============================================================
# Basic Heap Operations
# ============================================================

print("=== Basic Heap Operations ===")

# Create a heap from a list
arr = [5, 3, 8, 1, 2, 7]
heapq.heapify(arr)        # Convert list to heap IN-PLACE: O(n)
print(f"Heapified: {arr}")  # [1, 2, 7, 3, 5, 8] (min heap order)

# Peek at minimum (DON'T pop it)
print(f"Min element: {arr[0]}")  # 1 (always at index 0!)

# Push (add element)
heapq.heappush(arr, 0)
print(f"After push 0: {arr}")    # 0 is now the minimum

# Pop (remove and return minimum)
smallest = heapq.heappop(arr)
print(f"Popped: {smallest}")     # 0
print(f"After pop: {arr}")

# Push and Pop in one operation (more efficient)
result = heapq.heappushpop(arr, 4)  # push 4, then pop min
print(f"Pushpop(4): returned {result}")

# Get N smallest / N largest
nums = [10, 3, 7, 1, 9, 2, 8, 5, 4, 6]
print(f"\n3 smallest: {heapq.nsmallest(3, nums)}")  # [1, 2, 3]
print(f"3 largest:  {heapq.nlargest(3, nums)}")     # [10, 9, 8]


# ============================================================
# MAX HEAP trick: negate values
# ============================================================
"""
Python only has min heap. To simulate MAX HEAP:
  - Push NEGATIVE values: heappush(heap, -val)
  - Pop gives most negative = originally largest
  - Negate again when reading: -heappop(heap)
"""

print("\n=== Max Heap (using negation) ===")
max_heap = []
for val in [3, 1, 5, 2, 4]:
    heapq.heappush(max_heap, -val)  # negate!

print(f"Max element: {-max_heap[0]}")       # 5
print(f"Pop max: {-heapq.heappop(max_heap)}")  # 5
print(f"Pop max: {-heapq.heappop(max_heap)}")  # 4


# ============================================================
# Heap with Tuples (for priority queue)
# ============================================================
"""
heapq compares tuples element by element.
(priority, data) - lower priority number = higher priority
"""

print("\n=== Priority Queue with Tuples ===")
tasks = []
heapq.heappush(tasks, (3, "Low priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappush(tasks, (2, "Medium priority task"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  Priority {priority}: {task}")
# Prints in order: High, Medium, Low


"""
================================================================
SECTION 3: CLASSIC HEAP PROBLEMS
================================================================
"""


# ============================================================
# PROBLEM 1: Kth Largest Element in Array (LeetCode 215)
# ============================================================
"""
PROBLEM:
  Find the kth largest element in an unsorted array.
  
  Input:  [3, 2, 1, 5, 6, 4], k = 2
  Output: 5  (sorted: [1,2,3,4,5,6], 2nd largest = 5)

APPROACH: Min Heap of size K
  - Maintain a min heap of size k
  - The top (minimum) of this heap = kth largest overall
  
  Why? If we keep only the k largest elements in a min heap,
  the smallest of those k elements IS the kth largest.

VISUAL (k=2):
  Process [3, 2, 1, 5, 6, 4]:
  
  Push 3: heap = [3]            (size < k, just push)
  Push 2: heap = [2, 3]         (size = k)
  Push 1: 1 < heap[0]=2, skip   (too small to be in top-k)
  Push 5: 5 > heap[0]=2, pop 2, push 5: heap = [3, 5]
  Push 6: 6 > heap[0]=3, pop 3, push 6: heap = [5, 6]
  Push 4: 4 < heap[0]=5, skip
  
  Answer: heap[0] = 5 (2nd largest)
"""

def find_kth_largest(nums, k):
    # Method 1: Min heap of size k
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)  # pop min, push num
    
    return min_heap[0]

# TIME: O(n log k), SPACE: O(k)

# Method 2: Simple (but slower for large arrays)
def find_kth_largest_simple(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]
# TIME: O(n log n)


# ============================================================
# PROBLEM 2: Top K Frequent Elements (LeetCode 347)
# ============================================================
"""
PROBLEM:
  Find the k most frequent elements.
  
  Input:  nums = [1,1,1,2,2,3], k = 2
  Output: [1, 2]  (1 appears 3 times, 2 appears 2 times)
"""

from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    # nlargest by frequency
    return [item for item, freq in count.most_common(k)]

# Or using heap explicitly:
def top_k_frequent_heap(nums, k):
    count = Counter(nums)
    # Min heap of size k based on frequency
    return heapq.nlargest(k, count.keys(), key=count.get)

# TIME: O(n log k), SPACE: O(n)


# ============================================================
# PROBLEM 3: Merge K Sorted Lists (LeetCode 23)
# ============================================================
"""
PROBLEM:
  Merge k sorted linked lists into one sorted list.
  
  Input:  [[1,4,5], [1,3,4], [2,6]]
  Output: [1, 1, 2, 3, 4, 4, 5, 6]

APPROACH: Min Heap
  - Put first element of each list into heap
  - Pop smallest, add to result
  - Push next element from that list into heap
"""

def merge_k_sorted_lists(lists):
    """lists is a list of sorted Python lists (simplified version)."""
    min_heap = []
    
    # Push first element of each list with (value, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Push next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# TIME: O(N log k) where N = total elements, k = number of lists


# ============================================================
# PROBLEM 4: Find Median from Data Stream (LeetCode 295)
# ============================================================
"""
PROBLEM:
  Design a data structure that supports:
  - addNum(num): add a number
  - findMedian(): return the median of all added numbers

APPROACH: Two Heaps
  - Max heap (left half): stores smaller half of numbers
  - Min heap (right half): stores larger half of numbers
  - Median is at the tops of these heaps!
  
  Example: numbers = [2, 3, 1, 5, 4]
  
  After adding all:
    Max heap (left):  [2, 1]  -> top = 2
    Min heap (right): [3, 4, 5] -> top = 3
    
    Median = 3 (middle element since odd count)
"""

class MedianFinder:
    def __init__(self):
        self.left = []    # max heap (negate values)
        self.right = []   # min heap
    
    def addNum(self, num):
        # Push to max heap (left half)
        heapq.heappush(self.left, -num)
        
        # Ensure max of left <= min of right
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        
        # Balance sizes (left can have at most 1 more than right)
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
    
    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2


"""
================================================================
SUMMARY
================================================================

HEAP OPERATIONS:
  heapq.heapify(list)     O(n)       Convert list to min heap
  heapq.heappush(h, val)  O(log n)   Add element
  heapq.heappop(h)        O(log n)   Remove & return smallest
  h[0]                    O(1)       Peek at smallest
  heapq.nsmallest(k, h)   O(n log k) Get k smallest
  heapq.nlargest(k, h)    O(n log k) Get k largest

WHEN TO USE HEAP:
  - "Kth largest/smallest" problems
  - "Top K" problems
  - Merge K sorted things
  - Median finding
  - Scheduling / priority-based problems
  - Dijkstra's shortest path (Topic 11)
"""


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("HEAP PROBLEMS")
    print("=" * 60)
    
    print("\n--- Kth Largest ---")
    print(f"[3,2,1,5,6,4] k=2 -> {find_kth_largest([3,2,1,5,6,4], 2)}")  # 5
    
    print("\n--- Top K Frequent ---")
    print(f"[1,1,1,2,2,3] k=2 -> {top_k_frequent([1,1,1,2,2,3], 2)}")  # [1, 2]
    
    print("\n--- Merge K Sorted Lists ---")
    lists = [[1,4,5], [1,3,4], [2,6]]
    print(f"{lists} -> {merge_k_sorted_lists(lists)}")
    
    print("\n--- Median Finder ---")
    mf = MedianFinder()
    for num in [2, 3, 1, 5, 4]:
        mf.addNum(num)
        print(f"  Added {num}, median = {mf.findMedian()}")
    
    print("\nDone! Heaps complete!")

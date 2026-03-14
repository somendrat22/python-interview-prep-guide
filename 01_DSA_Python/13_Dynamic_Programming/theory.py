"""
================================================================
TOPIC 13: DYNAMIC PROGRAMMING (DP) - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS DYNAMIC PROGRAMMING?
================================================================

Dynamic Programming (DP) is a technique to solve problems by:
  1. Breaking them into OVERLAPPING SUBPROBLEMS
  2. Solving each subproblem ONCE
  3. STORING the result (so we don't recompute it)

Think of it like this:
  - Recursion: "I'll figure it out from scratch every time"
  - DP: "I'll remember answers I've already computed"

TWO KEY PROPERTIES (a problem must have BOTH for DP to apply):
  1. OPTIMAL SUBSTRUCTURE: Solution can be built from solutions to subproblems
  2. OVERLAPPING SUBPROBLEMS: Same subproblems are solved multiple times

Example - Fibonacci:
  fib(5) = fib(4) + fib(3)
  fib(4) = fib(3) + fib(2)  <-- fib(3) computed TWICE!
  
  Without DP: O(2^n) - recomputes everything
  With DP:    O(n) - computes each fib(i) only ONCE


================================================================
SECTION 2: TWO APPROACHES TO DP
================================================================

APPROACH 1: TOP-DOWN (Memoization)
  - Start from the big problem, break into smaller
  - Use RECURSION + CACHE (dictionary or array)
  - More natural / easier to think about
  - "Remember answers as you go"

APPROACH 2: BOTTOM-UP (Tabulation)
  - Start from smallest subproblems, build up to the answer
  - Use a TABLE (array) to store results
  - Usually slightly faster (no recursion overhead)
  - "Fill in a table from the bottom"

Both give the SAME result. Use whichever feels easier.


================================================================
SECTION 3: HOW TO APPROACH A DP PROBLEM
================================================================

STEP 1: Can I break this into smaller subproblems?
STEP 2: Define the STATE - what do I need to know at each step?
STEP 3: Define the RECURRENCE - how do states relate?
STEP 4: Define the BASE CASE - smallest subproblem I can solve directly
STEP 5: Decide direction - top-down or bottom-up?
STEP 6: Optimize space if possible
"""


# ============================================================
# EXAMPLE 1: Fibonacci (Classic DP Introduction)
# ============================================================

# --- Naive Recursion: O(2^n) - DON'T USE ---
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# --- Top-Down (Memoization): O(n) ---
def fib_memo(n, memo={}):
    """
    Same recursion, but CACHE results.
    Before computing, check if answer is already known.
    """
    if n in memo:
        return memo[n]       # already computed!
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# TIME: O(n), SPACE: O(n)


# --- Bottom-Up (Tabulation): O(n) ---
def fib_bottom_up(n):
    """
    Build answer from smallest subproblems.
    
    dp[i] = ith fibonacci number
    dp[0] = 0, dp[1] = 1
    dp[i] = dp[i-1] + dp[i-2]
    
    VISUAL:
      i:    0  1  2  3  4  5  6  7
      dp:   0  1  1  2  3  5  8  13
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# TIME: O(n), SPACE: O(n)


# --- Space Optimized: O(1) space ---
def fib_optimal(n):
    """We only need the last TWO values, not the whole array."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 1: Climbing Stairs (LeetCode 70) - DP Starter
# ============================================================
"""
PROBLEM:
  You can climb 1 or 2 steps at a time.
  How many distinct ways to reach the top (n steps)?
  
  n=1: 1 way  (1)
  n=2: 2 ways (1+1, 2)
  n=3: 3 ways (1+1+1, 1+2, 2+1)
  n=4: 5 ways

THINKING:
  To reach step n, you came from:
    - Step n-1 (took 1 step)
    - Step n-2 (took 2 steps)
  
  So: ways(n) = ways(n-1) + ways(n-2)
  This is just Fibonacci!
"""

def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 2: House Robber (LeetCode 198) - Classic DP
# ============================================================
"""
PROBLEM:
  You're a robber. Houses are in a row with money.
  You CANNOT rob two adjacent houses (alarm goes off).
  Maximize total money.
  
  Input:  [1, 2, 3, 1]
  Output: 4  (rob house 0 and house 2: 1 + 3 = 4)
  
  Input:  [2, 7, 9, 3, 1]
  Output: 12 (rob house 0, 2, 4: 2 + 9 + 1 = 12)

THINKING:
  At each house i, two choices:
    1. ROB it:  money[i] + best from house i-2 (skip adjacent)
    2. SKIP it: best from house i-1
  
  dp[i] = max money considering houses 0..i
  dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  
  Base: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])

VISUAL:
  nums = [2, 7, 9, 3, 1]
  
  dp[0] = 2
  dp[1] = max(2, 7) = 7
  dp[2] = max(dp[1], dp[0]+9) = max(7, 11) = 11
  dp[3] = max(dp[2], dp[1]+3) = max(11, 10) = 11
  dp[4] = max(dp[3], dp[2]+1) = max(11, 12) = 12
  
  Answer: 12
"""

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = curr
    
    return prev1

# TIME: O(n), SPACE: O(1)


# ============================================================
# PROBLEM 3: Coin Change (LeetCode 322) - Classic DP
# ============================================================
"""
PROBLEM:
  Given coin denominations and an amount, find MINIMUM coins needed.
  
  Input:  coins = [1, 5, 10, 25], amount = 30
  Output: 2  (25 + 5 = 30)
  
  Input:  coins = [2], amount = 3
  Output: -1 (impossible)

THINKING:
  dp[i] = minimum coins needed to make amount i
  
  For each amount i, try each coin:
    If coin <= i: dp[i] = min(dp[i], 1 + dp[i - coin])
    (1 coin + best way to make remaining amount)
  
  Base: dp[0] = 0 (0 coins to make amount 0)

VISUAL:
  coins = [1, 5, 10], amount = 11
  
  dp[0] = 0
  dp[1] = 1 (1 coin of 1)
  dp[2] = 2 (1+1)
  dp[3] = 3 (1+1+1)
  dp[4] = 4 (1+1+1+1)
  dp[5] = 1 (one 5-coin!)
  dp[6] = 2 (5+1)
  ...
  dp[10] = 1 (one 10-coin!)
  dp[11] = 2 (10+1)
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1

# TIME: O(amount * len(coins)), SPACE: O(amount)


# ============================================================
# PROBLEM 4: Longest Common Subsequence (LeetCode 1143)
# ============================================================
"""
PROBLEM:
  Find length of longest subsequence common to both strings.
  A subsequence can skip characters but maintains order.
  
  Input:  "abcde", "ace"
  Output: 3  (subsequence "ace")

THINKING:
  2D DP table: dp[i][j] = LCS of text1[0..i-1] and text2[0..j-1]
  
  If text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1  (both chars match, extend LCS)
  Else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char from either)

VISUAL:
       ""  a  c  e
  ""  [ 0, 0, 0, 0]
  a   [ 0, 1, 1, 1]
  b   [ 0, 1, 1, 1]
  c   [ 0, 1, 2, 2]
  d   [ 0, 1, 2, 2]
  e   [ 0, 1, 2, 3]  <- answer = 3
"""

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# TIME: O(m * n), SPACE: O(m * n)


# ============================================================
# PROBLEM 5: 0/1 Knapsack Problem (Classic DP)
# ============================================================
"""
PROBLEM:
  Given items with weights and values, and a knapsack capacity.
  Maximize total value without exceeding capacity.
  Each item can be taken at most ONCE.
  
  weights = [1, 3, 4, 5], values = [1, 4, 5, 7], capacity = 7
  Output: 9 (take items with weight 3 and 4: value 4+5=9)

THINKING:
  dp[i][w] = max value using items 0..i-1 with capacity w
  
  For each item, two choices:
    1. Don't take: dp[i][w] = dp[i-1][w]
    2. Take (if weight allows): dp[i][w] = dp[i-1][w-weight[i]] + value[i]
"""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# TIME: O(n * capacity), SPACE: O(n * capacity)


# ============================================================
# PROBLEM 6: Longest Increasing Subsequence (LeetCode 300)
# ============================================================
"""
PROBLEM:
  Find length of longest strictly increasing subsequence.
  
  Input:  [10, 9, 2, 5, 3, 7, 101, 18]
  Output: 4  (subsequence [2, 3, 7, 101] or [2, 5, 7, 101])

THINKING:
  dp[i] = length of LIS ending at index i
  
  For each j < i: if nums[j] < nums[i], then
    dp[i] = max(dp[i], dp[j] + 1)
"""

def length_of_lis(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # every element is an LIS of length 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# TIME: O(n^2), SPACE: O(n)
# There's an O(n log n) solution using binary search.


# ============================================================
# PROBLEM 7: Unique Paths (LeetCode 62)
# ============================================================
"""
PROBLEM:
  Robot at top-left of m x n grid. Can only move right or down.
  How many unique paths to bottom-right?
  
  dp[i][j] = dp[i-1][j] + dp[i][j-1]
  (paths from above + paths from left)
"""

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# TIME: O(m * n), SPACE: O(m * n)


"""
================================================================
SUMMARY - DP PATTERNS
================================================================

1. FIBONACCI-TYPE: Current depends on previous 1-2 states
   Examples: Climbing Stairs, House Robber, Fibonacci
   
2. KNAPSACK-TYPE: Choose items with constraint
   Examples: 0/1 Knapsack, Coin Change, Subset Sum
   
3. STRING DP: Compare two strings character by character
   Examples: LCS, Edit Distance, Longest Palindromic Subsequence
   
4. GRID DP: Move through a 2D grid
   Examples: Unique Paths, Minimum Path Sum, Maximal Square
   
5. INTERVAL DP: Solve subproblems on intervals
   Examples: Matrix Chain Multiplication, Burst Balloons

HOW TO RECOGNIZE DP:
  - "Count number of ways"
  - "Minimum/Maximum value"
  - "Is it possible to..."
  - "Longest/shortest ..."
  - Problem has optimal substructure + overlapping subproblems
"""


if __name__ == "__main__":
    print("=" * 60)
    print("DYNAMIC PROGRAMMING EXAMPLES")
    print("=" * 60)
    
    print(f"\n--- Fibonacci ---")
    print(f"fib(10) = {fib_optimal(10)}")  # 55
    
    print(f"\n--- Climbing Stairs ---")
    print(f"n=4: {climb_stairs(4)} ways")  # 5
    
    print(f"\n--- House Robber ---")
    print(f"[2,7,9,3,1] -> {rob([2,7,9,3,1])}")  # 12
    
    print(f"\n--- Coin Change ---")
    print(f"coins=[1,5,10] amount=11 -> {coin_change([1,5,10], 11)}")  # 2
    print(f"coins=[2] amount=3 -> {coin_change([2], 3)}")  # -1
    
    print(f"\n--- Longest Common Subsequence ---")
    print(f"'abcde','ace' -> {longest_common_subsequence('abcde','ace')}")  # 3
    
    print(f"\n--- Knapsack ---")
    print(f"w=[1,3,4,5] v=[1,4,5,7] cap=7 -> {knapsack([1,3,4,5],[1,4,5,7],7)}")  # 9
    
    print(f"\n--- Longest Increasing Subsequence ---")
    print(f"[10,9,2,5,3,7,101,18] -> {length_of_lis([10,9,2,5,3,7,101,18])}")  # 4
    
    print(f"\n--- Unique Paths ---")
    print(f"3x7 grid: {unique_paths(3, 7)} paths")  # 28
    
    print("\nDone! Dynamic Programming complete!")

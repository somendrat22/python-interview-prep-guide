"""
================================================================
TOPIC 8: RECURSION & BACKTRACKING - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS RECURSION?
================================================================

Recursion is when a function CALLS ITSELF to solve a smaller version
of the same problem.

Think of it like RUSSIAN NESTING DOLLS:
  - Open the big doll -> find a smaller doll inside
  - Open that -> find an even smaller doll
  - Keep going until you find the SMALLEST doll (base case)
  - Then put them back together (return results)

EVERY recursive function needs TWO things:
  1. BASE CASE - When to STOP (prevents infinite loop!)
  2. RECURSIVE CASE - Break problem into smaller subproblem
"""


# ============================================================
# SECTION 2: SIMPLE RECURSION EXAMPLES
# ============================================================

def countdown(n):
    """Print numbers from n down to 1."""
    if n <= 0:        # BASE CASE
        return
    print(n, end=" ")
    countdown(n - 1)  # RECURSIVE CASE


def factorial(n):
    """
    5! = 5 x 4 x 3 x 2 x 1 = 120
    
    factorial(4)
      = 4 * factorial(3)
      = 4 * (3 * factorial(2))
      = 4 * (3 * (2 * factorial(1)))
      = 4 * (3 * (2 * 1))  <-- base case
      = 24
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    fib(n) = fib(n-1) + fib(n-2)
    
    WARNING: Naive approach is O(2^n) - VERY SLOW!
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo={}):
    """Optimized fibonacci with memoization: O(n)"""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def recursive_sum(arr):
    """
    Sum of array using recursion.
    sum([1,2,3,4,5]) = 1 + sum([2,3,4,5]) = 1 + 2 + sum([3,4,5]) ...
    """
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])


def power(x, n):
    """
    Calculate x^n using fast power: O(log n)
    x^n = (x^(n/2))^2 if n is even
    x^n = x * x^(n-1) if n is odd
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        return x * power(x, n - 1)


"""
================================================================
SECTION 3: HOW TO THINK RECURSIVELY
================================================================

STEP-BY-STEP APPROACH:
  1. What is the SIMPLEST case? (base case)
  2. How can I break this into a SMALLER version of the same problem?
  3. How do I COMBINE the result of the smaller problem?

COMMON MISTAKES:
  X Forgetting the base case -> infinite recursion -> stack overflow
  X Base case doesn't cover all termination scenarios
  X Not making the problem SMALLER in recursive call

THE CALL STACK:
  Each recursive call adds a frame to the call stack.
  Python default limit is ~1000 recursive calls.
  import sys; sys.setrecursionlimit(10000) to increase.


================================================================
SECTION 4: BACKTRACKING
================================================================

Backtracking = recursion + UNDO.
  1. Make a choice
  2. Explore that path recursively
  3. If it doesn't work -> UNDO the choice (backtrack)
  4. Try the next option

Think of navigating a MAZE:
  - At each fork, pick a direction
  - If dead end -> go BACK and try another direction

TEMPLATE:
  def backtrack(current_state):
      if is_solution(current_state):
          save_solution()
          return
      for choice in available_choices:
          make_choice()          # DO
          backtrack(new_state)   # EXPLORE
          undo_choice()          # UNDO
"""


# ============================================================
# PROBLEM 1: Generate All Subsets (LeetCode 78)
# ============================================================
"""
PROBLEM:
  Given [1, 2, 3], generate ALL possible subsets.
  Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

APPROACH: For each element, include or exclude it.
"""

def subsets(nums):
    result = []
    
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])  # save a COPY
            return
        
        # Choice 1: Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        
        # Choice 2: Exclude (BACKTRACK - undo the include)
        current.pop()                  # UNDO!
        backtrack(index + 1, current)
    
    backtrack(0, [])
    return result

# TIME: O(2^n), SPACE: O(n)


# ============================================================
# PROBLEM 2: Generate All Permutations (LeetCode 46)
# ============================================================
"""
PROBLEM:
  Given [1, 2, 3], generate ALL orderings.
  Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

APPROACH: Pick each unused element as next, recurse, backtrack.
"""

def permutations(nums):
    result = []
    
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            # Choose remaining[i]
            current.append(remaining[i])
            # Explore with remaining elements (excluding chosen)
            backtrack(current, remaining[:i] + remaining[i+1:])
            # Undo choice
            current.pop()
    
    backtrack([], nums)
    return result

# TIME: O(n! * n), SPACE: O(n)


# ============================================================
# PROBLEM 3: Combination Sum (LeetCode 39)
# ============================================================
"""
PROBLEM:
  Given candidates = [2,3,6,7] and target = 7,
  find all unique combinations that sum to target.
  Same number can be used unlimited times.
  
  Output: [[2,2,3], [7]]
"""

def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            # Use i (not i+1) because we can reuse same element
            backtrack(i, current, remaining - candidates[i])
            current.pop()  # BACKTRACK
    
    backtrack(0, [], target)
    return result

# TIME: O(2^t) where t = target/min_candidate


# ============================================================
# PROBLEM 4: N-Queens (LeetCode 51) - Classic Backtracking!
# ============================================================
"""
PROBLEM:
  Place N queens on an NxN chess board so no two queens attack each other.
  Queens attack horizontally, vertically, and diagonally.
  
  For N=4, one solution:
  . Q . .
  . . . Q
  Q . . .
  . . Q .

APPROACH: Place queens row by row, check if position is safe.
"""

def solve_n_queens(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        """Check if placing queen at (row, col) is safe."""
        # Check column (all rows above)
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:
            # All queens placed successfully!
            solution = [''.join(r) for r in board]
            result.append(solution)
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'      # Place queen
                backtrack(row + 1)           # Try next row
                board[row][col] = '.'       # BACKTRACK (remove queen)
    
    backtrack(0)
    return result


# ============================================================
# PROBLEM 5: Word Search (LeetCode 79)
# ============================================================
"""
PROBLEM:
  Given a 2D board and a word, find if the word exists in the board.
  Can move up/down/left/right. Each cell used only once.
  
  board = [['A','B','C','E'],
           ['S','F','C','S'],
           ['A','D','E','E']]
  word = "ABCCED" -> True
"""

def word_search(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False
        
        # Mark as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore all 4 directions
        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))
        
        # BACKTRACK - restore cell
        board[r][c] = temp
        
        return found
    
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


# ============================================================
# SUMMARY
# ============================================================
"""
RECURSION:
  - Function calls itself with smaller input
  - ALWAYS need a base case
  - Think: "How is this problem a smaller version of itself?"

BACKTRACKING:
  - Recursion + undo choices
  - Try all possibilities, prune invalid paths
  - Template: choose -> explore -> unchoose

COMMON BACKTRACKING PROBLEMS:
  - Subsets, Permutations, Combinations
  - N-Queens, Sudoku Solver
  - Word Search, Palindrome Partitioning
  - Generate Parentheses
"""


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("RECURSION & BACKTRACKING EXAMPLES")
    print("=" * 60)
    
    print("\n--- Countdown ---")
    countdown(5)
    print()
    
    print("\n--- Factorial ---")
    print(f"5! = {factorial(5)}")       # 120
    print(f"10! = {factorial(10)}")     # 3628800
    
    print("\n--- Fibonacci ---")
    print(f"fib(10) = {fibonacci_memo(10)}")  # 55
    
    print("\n--- Recursive Sum ---")
    print(f"sum([1,2,3,4,5]) = {recursive_sum([1,2,3,4,5])}")  # 15
    
    print("\n--- Power ---")
    print(f"2^10 = {power(2, 10)}")    # 1024
    
    print("\n--- Subsets ---")
    print(f"subsets([1,2,3]) = {subsets([1, 2, 3])}")
    
    print("\n--- Permutations ---")
    print(f"permutations([1,2,3]) = {permutations([1, 2, 3])}")
    
    print("\n--- Combination Sum ---")
    print(f"candidates=[2,3,6,7] target=7 -> {combination_sum([2,3,6,7], 7)}")
    
    print("\n--- N-Queens (N=4) ---")
    solutions = solve_n_queens(4)
    for i, sol in enumerate(solutions):
        print(f"  Solution {i+1}:")
        for row in sol:
            print(f"    {row}")
    
    print("\n--- Word Search ---")
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(f"'ABCCED' -> {word_search(board, 'ABCCED')}")  # True
    
    print("\nDone! Recursion & Backtracking complete!")

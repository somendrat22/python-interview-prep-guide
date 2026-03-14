"""
================================================================
TOPIC 14: GREEDY ALGORITHMS - Complete Beginner Guide
================================================================

WHAT IS A GREEDY ALGORITHM?
  Makes the LOCALLY OPTIMAL choice at each step, hoping it leads
  to a GLOBALLY optimal solution. Unlike DP, it never looks back.

WHEN DOES GREEDY WORK?
  1. GREEDY CHOICE PROPERTY: Local optimal leads to global optimal
  2. OPTIMAL SUBSTRUCTURE: Optimal solution contains optimal sub-solutions
"""


# PROBLEM 1: Activity Selection / Max Meetings
# Sort by end time, always pick earliest finishing meeting.
def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    count = 0
    last_end = 0
    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end
    return count
# TIME: O(n log n), SPACE: O(1)


# PROBLEM 2: Jump Game (LeetCode 55)
# Track farthest reachable position.
def can_jump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True
# TIME: O(n), SPACE: O(1)


# PROBLEM 3: Jump Game II (LeetCode 45) - Minimum Jumps
def min_jumps(nums):
    if len(nums) <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps
# TIME: O(n), SPACE: O(1)


# PROBLEM 4: Best Time to Buy and Sell Stock II (LeetCode 122)
# Collect every upward price movement.
def max_profit_multiple(prices):
    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total += prices[i] - prices[i-1]
    return total
# TIME: O(n), SPACE: O(1)


# PROBLEM 5: Gas Station (LeetCode 134)
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
# TIME: O(n), SPACE: O(1)


# PROBLEM 6: Assign Cookies (LeetCode 455)
def find_content_children(g, s):
    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child
# TIME: O(n log n), SPACE: O(1)


# PROBLEM 7: Minimum Platforms (Train Schedule)
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = 0
    max_platforms = 0
    i = j = 0
    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return max_platforms


"""
SUMMARY - GREEDY vs DP:
  Greedy: Fast, simple, but only works for specific problems
  DP: Slower, more complex, works for more problems

COMMON GREEDY PROBLEMS:
  - Activity Selection / Meeting Rooms
  - Jump Game I & II
  - Stock Buy/Sell (unlimited transactions)
  - Gas Station, Assign Cookies
  - Huffman Coding, Fractional Knapsack
  - Minimum platforms, Task Scheduler
"""


if __name__ == "__main__":
    print("=" * 60)
    print("GREEDY ALGORITHM EXAMPLES")
    print("=" * 60)

    print(f"\n--- Max Meetings ---")
    meetings = [(0,6),(1,4),(3,5),(5,7),(5,9),(8,9)]
    print(f"{meetings} -> {max_meetings(meetings)}")

    print(f"\n--- Jump Game ---")
    print(f"[2,3,1,1,4] -> {can_jump([2,3,1,1,4])}")
    print(f"[3,2,1,0,4] -> {can_jump([3,2,1,0,4])}")

    print(f"\n--- Jump Game II ---")
    print(f"[2,3,1,1,4] -> {min_jumps([2,3,1,1,4])} jumps")

    print(f"\n--- Stock Profit (Multiple) ---")
    print(f"[7,1,5,3,6,4] -> {max_profit_multiple([7,1,5,3,6,4])}")

    print(f"\n--- Gas Station ---")
    print(f"gas=[1,2,3,4,5] cost=[3,4,5,1,2] -> start={can_complete_circuit([1,2,3,4,5],[3,4,5,1,2])}")

    print(f"\n--- Assign Cookies ---")
    print(f"g=[1,2,3] s=[1,1] -> {find_content_children([1,2,3],[1,1])}")

    print("\nDone! Greedy complete!")

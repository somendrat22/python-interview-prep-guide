"""
================================================================
TOPIC 11: GRAPHS (BFS, DFS) - Complete Beginner Guide
================================================================

================================================================
SECTION 1: WHAT IS A GRAPH?
================================================================

A Graph is a collection of NODES (vertices) connected by EDGES.

Think of it like a MAP:
  - Cities are NODES
  - Roads between cities are EDGES

VISUAL:
    A --- B
    |   / |
    |  /  |
    C --- D

  Nodes: {A, B, C, D}
  Edges: {A-B, A-C, B-C, B-D, C-D}

TERMINOLOGY:
  - VERTEX (Node): A point in the graph (A, B, C, D)
  - EDGE: Connection between two vertices (A-B)
  - ADJACENT: Two nodes connected by an edge (A and B are adjacent)
  - DEGREE: Number of edges connected to a node
  - PATH: Sequence of vertices connected by edges (A -> B -> D)
  - CYCLE: Path that starts and ends at the same vertex (A -> B -> C -> A)
  - CONNECTED: Every node is reachable from every other node


================================================================
SECTION 2: TYPES OF GRAPHS
================================================================

1. UNDIRECTED GRAPH: Edges have NO direction
   A --- B  (can go A->B and B->A)

2. DIRECTED GRAPH (Digraph): Edges have direction (arrows)
   A --> B  (can only go A->B, NOT B->A)

3. WEIGHTED GRAPH: Edges have weights/costs
   A --5-- B  (cost to travel from A to B is 5)

4. UNWEIGHTED GRAPH: All edges have equal weight

5. CYCLIC: Contains at least one cycle
6. ACYCLIC: No cycles (DAG = Directed Acyclic Graph)


================================================================
SECTION 3: HOW TO REPRESENT A GRAPH IN CODE
================================================================

Two main ways:

METHOD 1: ADJACENCY LIST (Most Common in Interviews!)
  Use a dictionary where:
    key = node
    value = list of neighbors

METHOD 2: ADJACENCY MATRIX
  Use a 2D array where:
    matrix[i][j] = 1 means edge from i to j
    matrix[i][j] = 0 means no edge

  Adjacency List is preferred because:
    - Less memory for sparse graphs
    - Easier to iterate over neighbors
    - Most interview problems use it
"""

from collections import deque, defaultdict


# ============================================================
# Building a Graph
# ============================================================

# Undirected graph using adjacency list
def build_undirected_graph(edges):
    """
    edges = [(A, B), (A, C), (B, D), ...]
    
    Result:
    {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A'],
      'D': ['B']
    }
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected = add both ways
    return graph


# Directed graph
def build_directed_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # only one direction
    return graph


# From adjacency matrix to list
def matrix_to_adj_list(matrix):
    """
    matrix = [[0,1,1],    node 0 connects to 1, 2
              [1,0,0],    node 1 connects to 0
              [1,0,0]]    node 2 connects to 0
    """
    n = len(matrix)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph


"""
================================================================
SECTION 4: GRAPH TRAVERSALS - BFS & DFS
================================================================

These are the TWO fundamental ways to explore a graph.
You MUST know both inside out.

BFS (Breadth-First Search):
  - Explore level by level (like ripples in water)
  - Uses a QUEUE
  - Finds SHORTEST PATH in unweighted graphs

DFS (Depth-First Search):
  - Explore as deep as possible, then backtrack
  - Uses a STACK (or recursion)
  - Good for: cycle detection, topological sort, connected components
"""


# ============================================================
# BFS - Breadth-First Search
# ============================================================
"""
VISUAL:
  Graph:    A --- B
            |   / |
            |  /  |
            C --- D

  BFS starting from A:
  
  Queue: [A]                Visit A. Add neighbors B, C.
  Queue: [B, C]             Visit B. Add neighbor D (A,C already visited).
  Queue: [C, D]             Visit C. (All neighbors visited).
  Queue: [D]                Visit D. (All neighbors visited).
  Queue: []                 Done!
  
  Visit order: A, B, C, D (level by level)
"""

def bfs(graph, start):
    """BFS traversal of a graph."""
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order

# TIME: O(V + E) where V = vertices, E = edges
# SPACE: O(V)


# ============================================================
# DFS - Depth-First Search
# ============================================================
"""
VISUAL:
  Graph:    A --- B
            |   / |
            |  /  |
            C --- D

  DFS starting from A:
  
  Visit A -> go to B (first neighbor)
    Visit B -> go to C (first unvisited neighbor)
      Visit C -> go to D (first unvisited neighbor)
        Visit D -> all neighbors visited, BACKTRACK
      Back to C -> all done, BACKTRACK
    Back to B -> all done, BACKTRACK
  Back to A -> all done.
  
  Visit order: A, B, C, D (goes deep first)
"""

# DFS Recursive (most natural)
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    order = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    
    return order


# DFS Iterative (using explicit stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            
            # Add neighbors to stack (reverse for consistent order)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return order

# TIME: O(V + E), SPACE: O(V)


"""
================================================================
SECTION 5: CLASSIC GRAPH PROBLEMS
================================================================
"""


# ============================================================
# PROBLEM 1: Number of Islands (LeetCode 200) - VERY COMMON!
# ============================================================
"""
PROBLEM:
  Given a 2D grid of '1' (land) and '0' (water),
  count the number of islands.
  An island is surrounded by water and formed by connecting
  adjacent land cells horizontally or vertically.
  
  Input:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
  
  Output: 3 (three separate islands)

APPROACH:
  - Scan the grid. When we find a '1' (land):
    1. Increment island count
    2. BFS/DFS to mark ALL connected land as visited
  - Continue scanning for next unvisited land
"""

def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        """Mark all connected land as visited by changing '1' to '0'."""
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'  # mark as visited
        
        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # mark entire island as visited
    
    return count

# TIME: O(rows * cols), SPACE: O(rows * cols) worst case recursion


# ============================================================
# PROBLEM 2: BFS Shortest Path in Unweighted Graph
# ============================================================
"""
PROBLEM:
  Find shortest path from source to destination in an unweighted graph.
  
  BFS naturally finds shortest path because it explores level by level.
  Level 0: source
  Level 1: all nodes 1 step away
  Level 2: all nodes 2 steps away
  ...
"""

def shortest_path_bfs(graph, start, end):
    if start == end:
        return [start]
    
    visited = set([start])
    queue = deque([(start, [start])])  # (node, path_so_far)
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []  # no path found

# TIME: O(V + E), SPACE: O(V)


# ============================================================
# PROBLEM 3: Detect Cycle in Undirected Graph
# ============================================================
"""
APPROACH: DFS with parent tracking.
If we visit a node that's already visited AND it's not our parent,
there's a cycle.
"""

def has_cycle_undirected(graph, num_nodes):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # visited and not parent = CYCLE!
        return False
    
    # Check all components (graph might be disconnected)
    for node in range(num_nodes):
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


# ============================================================
# PROBLEM 4: Topological Sort (for DAGs)
# ============================================================
"""
PROBLEM:
  Order nodes so that for every directed edge u->v, u comes before v.
  Only possible for DAGs (Directed Acyclic Graphs).
  
  Used for: task scheduling, build systems, course prerequisites.
  
  Example: Course prerequisites
    Course 1 requires Course 0.
    Course 2 requires Course 0.
    Course 3 requires Course 1 and Course 2.
    
    Valid order: 0, 1, 2, 3 or 0, 2, 1, 3

APPROACH: Kahn's Algorithm (BFS with in-degree)
  1. Calculate in-degree (number of incoming edges) for each node
  2. Add all nodes with in-degree 0 to queue
  3. Process queue: remove node, decrease in-degree of neighbors
  4. If neighbor's in-degree becomes 0, add to queue
"""

def topological_sort(num_nodes, edges):
    """edges = [(prerequisite, course), ...]"""
    graph = defaultdict(list)
    in_degree = [0] * num_nodes
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Start with nodes that have no prerequisites
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If order contains all nodes, valid topological sort exists
    if len(order) == num_nodes:
        return order
    return []  # cycle exists, no valid ordering

# TIME: O(V + E), SPACE: O(V + E)


# ============================================================
# PROBLEM 5: Clone Graph (LeetCode 133)
# ============================================================
"""
PROBLEM: Create a deep copy of a graph.

APPROACH: BFS/DFS with a hashmap to track old_node -> new_node mapping.
"""

def clone_graph(node):
    """node is a graph node with .val and .neighbors list."""
    if not node:
        return None
    
    cloned = {}  # old node -> new node
    queue = deque([node])
    
    # Create clone of starting node
    cloned[node] = type(node)(node.val)
    
    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = type(neighbor)(neighbor.val)
                queue.append(neighbor)
            cloned[current].neighbors.append(cloned[neighbor])
    
    return cloned[node]


"""
================================================================
SUMMARY
================================================================

BFS vs DFS:
  BFS: Queue, level-by-level, shortest path in unweighted graphs
  DFS: Stack/recursion, go deep first, cycle detection, topological sort

GRAPH REPRESENTATION:
  Adjacency List: dict of lists (preferred)
  Adjacency Matrix: 2D array

COMMON PROBLEMS:
  - Number of Islands (DFS/BFS on grid)
  - Shortest Path (BFS)
  - Cycle Detection (DFS)
  - Topological Sort (Kahn's BFS)
  - Connected Components
  - Clone Graph
  - Course Schedule (LeetCode 207, 210)

TIME: O(V + E) for both BFS and DFS
SPACE: O(V) for visited set + queue/stack
"""


if __name__ == "__main__":
    print("=" * 60)
    print("GRAPH EXAMPLES")
    print("=" * 60)
    
    # Build graph
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    graph = build_undirected_graph(edges)
    print(f"\nGraph: {dict(graph)}")
    
    print(f"\n--- BFS from A ---")
    print(f"Order: {bfs(graph, 'A')}")
    
    print(f"\n--- DFS from A (recursive) ---")
    print(f"Order: {dfs_recursive(graph, 'A')}")
    
    print(f"\n--- DFS from A (iterative) ---")
    print(f"Order: {dfs_iterative(graph, 'A')}")
    
    print(f"\n--- Shortest Path A to D ---")
    print(f"Path: {shortest_path_bfs(graph, 'A', 'D')}")
    
    print(f"\n--- Number of Islands ---")
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    print(f"Islands: {num_islands(grid)}")  # 3
    
    print(f"\n--- Topological Sort ---")
    # Course 0 is prereq for 1, 2. Course 1,2 are prereqs for 3.
    topo_edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    print(f"Order: {topological_sort(4, topo_edges)}")  # [0, 1, 2, 3] or similar
    
    print("\nDone! Graphs complete!")

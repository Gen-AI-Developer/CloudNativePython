# Data Structures and Algorithms in Python: A Comprehensive Guide

## Table of Contents
1. [Basic Data Structures](#basic-data-structures)
2. [Advanced Data Structures](#advanced-data-structures)
3. [Searching Algorithms](#searching-algorithms)
4. [Sorting Algorithms](#sorting-algorithms)
5. [Graph Algorithms](#graph-algorithms)
6. [Dynamic Programming](#dynamic-programming)
7. [Time & Space Complexity](#complexity)

## Basic Data Structures

### Lists
Lists are built-in dynamic arrays in Python.

```python
# List operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)        # O(1)
numbers.insert(0, 0)     # O(n)
numbers.pop()           # O(1)
numbers.pop(0)          # O(n)
numbers.index(3)        # O(n)
```

### Strings
Strings are immutable sequences of characters.

```python
# String operations
text = "hello"
reversed_text = text[::-1]  # Reverse string
substring = text[1:4]       # Slice string
```

### Dictionaries
Dictionaries implement hash tables for key-value storage.

```python
# Dictionary operations
cache = {}
cache['key'] = 'value'   # O(1) average
value = cache.get('key') # O(1) average
del cache['key']         # O(1) average
```

### Sets
Sets store unique elements in an unordered collection.

```python
# Set operations
unique_numbers = {1, 2, 3}
unique_numbers.add(4)      # O(1) average
unique_numbers.remove(1)   # O(1) average
```

## Advanced Data Structures

### Stack (using list)
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
```

### Queue (using collections.deque)
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft() if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
```

### LinkedList
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
```

## Searching Algorithms

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found
```

### Linear Search
```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1  # Target not found
```

## Sorting Algorithms

### Quick Sort
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
```

### Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
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
```

## Graph Algorithms

### Graph Implementation
```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
```

### Breadth-First Search (BFS)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Depth-First Search (DFS)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

## Dynamic Programming

### Fibonacci (with memoization)
```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

### Longest Common Subsequence
```python
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

## Time & Space Complexity

### Common Time Complexities
- O(1): Constant time
- O(log n): Logarithmic time
- O(n): Linear time
- O(n log n): Linearithmic time
- O(n²): Quadratic time
- O(2ⁿ): Exponential time

### Data Structure Operations
#### Lists
- Append: O(1)
- Insert/Delete at beginning: O(n)
- Access by index: O(1)
- Search: O(n)

#### Dictionaries
- Insert/Delete/Access: O(1) average
- Search: O(1) average

#### Binary Search Tree
- Insert/Delete/Search: O(log n) average, O(n) worst

Remember that these complexities are average cases. Worst-case scenarios might have different complexities.

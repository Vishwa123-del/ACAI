class Graph:
    def __init__(self):
        """Initialize an empty graph with adjacency list representation."""
        self.adj_list = {}
    def add_edge(self, u, v):
        """Add an edge from u to v (undirected by default)."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def bfs(self, start):
        """Perform Breadth-First Search starting from the given node."""
        from collections import deque
        visited = set()  # Track visited nodes
        queue = deque([start])  # Queue for BFS
        order = []  # List to store traversal order
        while queue:
            node = queue.popleft()
            if node not in visited:
                # Visit the node and add to order
                visited.add(node)
                order.append(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order
    def dfs_iterative(self, start):
        """Perform iterative Depth-First Search starting from the given node."""
        visited = set()
        stack = [start]  # Use a stack for DFS
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                # Visit the node and add to order
                visited.add(node)
                order.append(node)
                # Add neighbors to stack (reverse for consistent ordering)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order
    def dfs_recursive(self, start):
        """Perform recursive Depth-First Search starting from the given node."""
        visited = set()
        order = []
        def dfs(node):
            if node not in visited:
                # Visit the node and add to order
                visited.add(node)
                order.append(node)
                # Recursively visit all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)
        dfs(start)
        return order
# Example usage and comparison
if __name__ == "__main__":
    g = Graph()
    # Create a sample undirected graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    print("Adjacency List:", g.adj_list)
    print("BFS traversal from node 0:", g.bfs(0))
    print("Iterative DFS traversal from node 0:", g.dfs_iterative(0))
    print("Recursive DFS traversal from node 0:", g.dfs_recursive(0))

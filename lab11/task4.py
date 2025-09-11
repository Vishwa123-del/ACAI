class Node:
    def __init__(self, data):
        """Initialize a node with data and optional left/right children."""
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, data):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        """Helper method to insert recursively."""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        # If data == node.data, do not insert duplicates

    def search(self, data):
        """Search for a value in the BST. Returns True if found, else False."""
        return self._search(self.root, data)

    def _search(self, node, data):
        """Helper method to search recursively."""
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder_traversal(self):
        """Return a list of all elements in the BST in sorted order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

# --- Test Cases ---
if __name__ == "__main__":
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for num in nums:
        bst.insert(num)
    print("Inorder traversal (should be sorted):", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]

    # Test search for present elements
    print("Search 60:", bst.search(60))  # True
    print("Search 30:", bst.search(30))  # True

    # Test search for absent elements
    print("Search 25:", bst.search(25))  # False
    print("Search 90:", bst.search(90))  # False

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Each node starts with a height of 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the AVL tree."""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Update the height of the current node
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Get the balance factor to check for imbalance
        balance = self._balance(node)

        # Left-Left Case
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        # Right-Right Case
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        # Left-Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        """Perform a left rotation."""
        assert z and z.right, "Cannot perform left rotation on None or invalid node"
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_right(self, z):
        """Perform a right rotation."""
        assert z and z.left, "Cannot perform right rotation on None or invalid node"
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _height(self, node):
        """Get the height of a node."""
        return node.height if node else 0

    def _balance(self, node):
        """Calculate the balance factor of a node."""
        return self._height(node.left) - self._height(node.right) if node else 0

    def search(self, value):
        """Search for a value in the AVL tree."""
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder_traversal(self):
        """Perform an in-order traversal of the AVL tree."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

# Testing the AVL Tree
if __name__ == "__main__":
    elements = [10, 20, 30, 40, 50, 25]
    avl_tree = AVLTree()

    print("Inserting elements:", elements)
    for elem in elements:
        avl_tree.insert(elem)

    print("In-order traversal of the AVL tree:", avl_tree.inorder_traversal())
    search_value = 25
    print(f"Searching for {search_value}:", "Found" if avl_tree.search(search_value) else "Not Found")

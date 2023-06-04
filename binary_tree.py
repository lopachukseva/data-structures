class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node with value: {self.data}"


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def _find(self, node, parent, data):
        if node is None:
            return None, parent, False

        if data == node.data:
            return node, parent, True

        if data < node.data:
            if node.left:
                return self._find(node.left, node, data)

        if data > node.data:
            if node.right:
                return self._find(node.right, node, data)

        return node, parent, False

    def add_element(self, node):
        if self.root is None:
            self.root = node
            return node

        s, p, is_find = self._find(self.root, None, node.data)

        if not is_find and s:
            if node.data < s.data:
                s.left = node
            else:
                s.right = node

        return node

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


s = [8, 4, 5, 6, 13, 12, 19, 13, 11]

bt = BinaryTree()

for num in s:
    print(bt.add_element(Node(num)))

bt.show_tree(bt.root)

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

        # s - scion, p - parent
        s, p, is_find = self._find(self.root, None, node.data)

        if not is_find and s:
            if node.data < s.data:
                s.left = node
            else:
                s.right = node

        return node

    def show_tree_deep(self, node):
        if node is None:
            return

        self.show_tree_deep(node.left)
        print(node.data)
        self.show_tree_deep(node.right)

    def show_tree_wide(self):
        v = [self.root]

        while v:
            vn = []

            for node in v:
                print(node.data, end=" ")
                if node.left:
                    vn.append(node.left)
                if node.right:
                    vn.append(node.right)
            print("")
            v = vn

    @staticmethod
    def _del_leaf(s, p):
        if p.left == s:
            p.left = None
        else:
            p.right = None

    @staticmethod
    def _del_one_child(s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def _find_min(self, node, parent):
        if node.left:
            return self._find_min(node.left, node)
        else:
            return node, parent

    def del_node(self, key):
        s, p, is_find = self._find(self.root, None, key)

        if not is_find:
            return None
        else:
            if s.left is None and s.right is None:
                self._del_leaf(s, p)
            elif s.left is None or s.right is None:
                self._del_one_child(s, p)
            else:
                # sr - scion right, pr - parent right
                sr, pr = self._find_min(s.right, s)
                s.data = sr.data
                self._del_one_child(sr, pr)


if __name__ == "__main__":
    s = [8, 4, 5, 6, 13, 12, 19, 13, 11]

    bt = BinaryTree()

    for num in s:
        bt.add_element(Node(num))

    print("Before del:")
    bt.show_tree_deep(bt.root)
    bt.del_node(5)
    bt.del_node(12)

    print("After del:")
    bt.show_tree_deep(bt.root)

    print("Wide:")
    bt.show_tree_wide()

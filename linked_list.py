class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_next_node(self, new_node):
        self.next = new_node

    def get_next(self):
        return self.next

    def __str__(self):
        return f"[{self.data}] -> {self.get_next()}"


class LinkedList:
    def __init__(self, first_node_data):
        self.head = Node(first_node_data)
        self.last_element = self.head
        self.length = 1

    def add_node(self, node_data):
        new_node = Node(node_data)
        self.last_element.add_next_node(new_node)
        self.last_element = new_node
        self.length += 1

    def __str__(self):
        return f'[{self.head.data}] -> {self.head.get_next()}'

    def __len__(self):
        return self.length

    # def get_length(self):
    #     node = self.head
    #     length = 0
    #     while node is not None:
    #         node = node.get_next()
    #         length += 1
    #     return length

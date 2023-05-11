from linked_list import Node, LinkedList


def reverse_linked_list(head: Node):
    tail = head
    next_node = head.next
    tail.next = None
    prev_node = tail

    while True:
        next_next_node = next_node.next
        next_node.next = prev_node
        prev_node = next_node
        next_node = next_next_node

        if next_node is None:
            break

    head = prev_node

    return head


my_list = LinkedList("Hello! I am first node!")
my_list.add_node("Hello! I am second node!")
my_list.add_node("Hello! I am third node!")
my_list.add_node("Hello! I am a fourth node!")

print(my_list)
print(reverse_linked_list(my_list.head))

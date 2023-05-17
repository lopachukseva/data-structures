class Queue:
    def __init__(self):
        self._elements = []

    def add_item(self, item):
        self._elements.append(item)

    def get_item(self):
        if len(self._elements) != 0:
            return self._elements.pop(0)
        else:
            return None

    def __len__(self):
        return len(self._elements)


q = Queue()

q.add_item(1)
q.add_item(2)
q.add_item(3)
q.add_item(4)
q.add_item(5)

print(len(q))

print(q.get_item())
print(q.get_item())
print(q.get_item())
print(q.get_item())
print(q.get_item())
print(q.get_item())

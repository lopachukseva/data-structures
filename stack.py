class Stack:
    def __init__(self):
        self._elements = []

    def add_item(self, item):
        self._elements.append(item)

    def get_item(self):
        if len(self._elements) != 0:
            return self._elements.pop()
        else:
            return None

    def __len__(self):
        return len(self._elements)


s = Stack()

s.add_item(1)
s.add_item(2)
s.add_item(3)
s.add_item(4)
s.add_item(5)

print(len(s))

print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())

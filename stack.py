class Stack:
    def __init__(self):
        self.elements = []

    def add_item(self, item):
        self.elements.append(item)

    def get_item(self):
        if len(self.elements) != 0:
            return self.elements.pop()
        else:
            return None


s = Stack()

s.add_item(1)
s.add_item(2)
s.add_item(3)
s.add_item(4)
s.add_item(5)


print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())
print(s.get_item())

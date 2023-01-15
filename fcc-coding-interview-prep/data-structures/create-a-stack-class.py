class Stack():
    def __init__(self) -> None:
        self.collection = []

    def print(self):
        print(self.collection)

    def push(self, el):
        self.collection.append(el)

    def pop(self):
        return self.collection.pop()

    def peek(self):
        return self.collection[-1]

    def is_empty(self):
        return len(self.collection) == 0

    def clear(self):
        return self.collection.clear()


test = Stack()
test.push(1)
test.push(2)
test.push(5)
print(test.peek())

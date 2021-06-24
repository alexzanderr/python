

class Stack:
    def __init__(self, *objects):
        self.stack = []
        if len(objects) > 0:
            for obj in objects:
                self.stack.append(obj)


    def push(self, *objects):
        for obj in objects:
            self.queue.append(obj)


    def pop(self, obj):
        if self.queue != []:
            self.stack.pop()


    def top_item(self):
        if self.queue != []:
            return self.stack[len(self.stack) - 1]


    def isempty(self):
        return self.stack == 0


    def dimension(self):
        return len(self.stack)


    def clear(self):
        self.stack.clear()


    def __str__(self):
        return self.stack.__str__()


    def __repr__(self):
        return self.stack.__repr__()


    def __eq__(self, Stack_instance):
        return self.stack == Stack_instance.stack


# usage
if __name__ == '__main__':
    q = Stack()
    q2 = Stack(1, 2, 3, 4, 5, 6, 7, 8)
    print(q)
    print(q2)

    q3 = Stack(1, 2, 3, 4, *[1, 2, 3, 4, 5], Stack(1, 2, 3, 4))
    print(q3)
    print(q == q3)
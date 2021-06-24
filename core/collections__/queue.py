

class Queue:
    def __init__(self, *objects):
        self.queue = []
        if len(objects) > 0:
            for obj in objects:
                self.queue.append(obj)


    def pop_front(self):
        self.queue = self.queue[1:]


    def append_back(self, *objects):
        for obj in objects:
            self.queue.append(obj)


    def front(self):
        if self.queue != []:
            return self.queue[0]

    def last(self):
        if self.queue != []:
            return self.queue[len(self.queue) - 1]


    def dimension(self):
        return len(self.queue)


    def clear(self):
        self.queue.clear()

    def isempty(self):
        return self.queue == []


    def __str__(self):
        return self.queue.__str__()


    def __repr__(self):
        return self.queue.__repr__()


    def __eq__(self, Queue_instance):
        return self.queue == Queue_instance.queue


# TESTING
if __name__ == '__main__':
    q = Queue(2, 3, 4, 5, 5, 6)
    print(q)

    q.pop_front()
    print(q)

    q.append_back()
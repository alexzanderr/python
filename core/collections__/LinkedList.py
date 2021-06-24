

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        content = f"Node({self.data})"
        return content


class LinkedList:
    def __init__(self):
        self.head = Node()


    def append(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)


    def __len__(self):
        current_node = self.head
        length = 0
        while current_node.next:
            length += 1
            current_node = current_node.next
        return length


    def __str__(self):
        content = "["
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            content += str(current_node.data) + "->"
        content = content[:len(content) - 2] + "]"
        if content:
            return content
        return "there is just an empty head"


    def __getitem__(self, index: int):
        if not (0 <= index <= len(self) - 1):
            raise IndexError("linked list out of range in getting item")
        current_index = 0
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1


    # concatenating two linked lists
    def __add__(self, other_head):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = other_head.head.next
        return self


    # deletes the item and returns it
    def __delitem__(self, index):
        """ how to use: 'del linked_list[eBookIndex]' """
        if not (0 <= index <= len(self) - 1):
            raise IndexError("linked list out of range in deleting item")
        current_index = 0
        current_node = self.head
        while current_node.next:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return current_node.data
            current_index += 1


    def delete_item(self, index):
        del self[index]


    def insert_item(self, data, index):
        if not (0 <= index <= len(self) - 1):
            raise IndexError("linked list out of range on inserting an item")
        if not data:
            raise ValueError("None value on inserting an item")

        current_index = 0
        current_node = self.head
        while current_node.next:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                new_node = Node(data)
                last_node.next = new_node
                new_node.next = current_node
                return
            current_index += 1


    def insert_node(self, node: Node, index):
        if not (0 <= index <= len(self) - 1):
            raise IndexError("linked list out of range on inserting an item")
        if not node.data:
            raise ValueError("None value on inserting an item")

        current_index = 0
        current_node = self.head
        while current_node.next:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = node
                node.next = current_node
                return
            current_index += 1


    # returns the old item
    def overwrite_item(self, index, data):
        if not (0 <= index <= len(self) - 1):
            raise IndexError("linked list out of range on inserting an item")
        if not data:
            raise ValueError("None value on inserting an item")

        current_index = 0
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            if current_index == index:
                old_item = current_node.data
                current_node.data = data
                return old_item
            current_index += 1


# TESTING
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(123)
    ll.append(676)
    ll.append(23)
    ll.append(23123)
    ll.append(2323)
    ll.append(2320000003)
    print(ll)
    for index in range(len(ll)):
        print(index, "=>", end='')
    print()
    ll.insert_item(74, 1)
    print(ll)

    item = Node(1)
    print(item)

    ll.insert_node(item, 4)
    print(ll)

    ll.overwrite_item(1, 7474)
    print(ll)
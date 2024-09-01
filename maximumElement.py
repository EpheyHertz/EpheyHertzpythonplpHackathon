class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head
        # Traverse the list to find the last node
        while last.next:
            last = last.next
        # Append the new node at the end
        last.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The list is empty")
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value


li = LinkedList()
li.append(3)
li.append(1)
li.append(6)
li.append(5)
li.append(4)


print(li.find_max())

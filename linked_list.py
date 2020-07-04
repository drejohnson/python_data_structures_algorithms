class Node:

    # Initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

     # Reverse linked list
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # print middle value in linked list
    def print_middle(self):
        temp_head = self.head
        count = 0

        while self.head:
            # only update when count is odd
            print(f"count & 1: {count & 1}")
            if (count & 1):
                temp_head = temp_head.next
                print(f"temp_head: {temp_head.data}")

            self.head = self.head.next

            # increment count in each iteration
            count += 1

        print(temp_head.data)

    # count the occurrences of a item in linked list
    def count(self, item):
        current = self.head
        count = 0
        while current:
            if (current.data == item):
                count += 1
            current = current.next
        print(f"count: {count}")

    # print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next


s_ll = LinkedList()
s_ll.push(1)
s_ll.push(2)
s_ll.push(3)
s_ll.push(4)
s_ll.push(5)
s_ll.push(6)
s_ll.push(4)
s_ll.push(8)
s_ll.push(4)

s_ll.print_list()
s_ll.reverse_list()
s_ll.count(4)

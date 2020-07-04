

class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
      
class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # create Node and and make linked list 
    def push(self, new_value): 
        new_node = Node(new_value) 
        new_node.next = self.head 
        self.head = new_node 
          
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
          
s_ll = LinkedList()  
s_ll.push(5) 
s_ll.push(25)  
s_ll.push(65)  
s_ll.push(15)  
s_ll.push(35)
s_ll.push(69) 
s_ll.push(75)
s_ll.print_middle() 
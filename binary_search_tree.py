from queue import Queue
from stack import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        self.root = Node(value)
        self.count = 1


    def size(self):
        print(self.count)  # returns the number of items in tree


    def insert(self, value):
        self.count += 1

        new_node = Node(value)

        def search_tree(node):
            # if value <  node.value, go left
            if value < node.value:
                # if left child doesn't exist, append new node
                if node.left is None:
                    node.left = new_node
                # if left child exist, recursively look left again
                else:
                    search_tree(node.left)

            # value > node.value, go right
            if value >= node.value:
                # if right child doesn't exist, append new node
                if node.right is None:
                    node.right = new_node
                else:
                    search_tree(node.right)

        # invoke recursive function
        search_tree(self.root)


    def min_value(self):
        current_node = self.root

        # traverse left until no more children
        while(current_node.left):
            current_node = current_node.left

        print(f"min value: {current_node.value}")


    def max_value(self):
        current_node = self.root

        # traverse right until no more children
        while(current_node.right):
            current_node = current_node.right

        print(f"max value: {current_node.value}")


    def contains(self, value):
        current_node = self.root

        while current_node:
            # if value is found return true
            if value == current_node.value:
                print(f"contains {value}: {True}")
                return True

            # if value < current node value, look left
            if value < current_node.value:
                current_node = current_node.left

            # else, look right
            else:
                current_node = current_node.right

        # if value not found return false
        print(f"contains {value}: {False}")
        return False


    def for_each(self, cb):

        def traverse_tree(node):
            # instantiate cb
            cb(node.value)

            # if left child exist, go left again and again
            if node.left:
                traverse_tree(node.left)

            # right child exist, go right again and again
            if node.right:
                traverse_tree(node.right)

        # invoke recursive function
        traverse_tree(self.root)

        return cb

    # depth first search - branch by branch

    # print values iteratively
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            popped = stack.pop()

            print(popped.value)

            if popped.left:
                stack.push(popped.left)

            if popped.right:
                stack.push(popped.right)

    # in-order
    # left - root - right
    def dfs_in_order(self):
        result = []

        # Could extract this function - DRY
        def traverse_tree(node):
            # if left child exist, go left again and again
            if node.left:
                traverse_tree(node.left)

            # capture root node value
            result.append(node.value)

            # right child exist, go right again and again
            if node.right:
                traverse_tree(node.right)

        # invoke recursive function
        traverse_tree(self.root)

        print(f"dfs_in_order: {result}")
        return result

    # pre-order
    # root - left - right
    def dfs_pre_order(self):
        result = []

        def traverse_tree(node):
            # capture root node value
            result.append(node.value)

            # if left child exist, go left again and again
            if node.left:
                traverse_tree(node.left)

            # right child exist, go right again and again
            if node.right:
                traverse_tree(node.right)

        # invoke recursive function
        traverse_tree(self.root)

        print(f"dfs_pre_order: {result}")
        return result


    # post-order
    # left - right - root
    def dfs_post_order(self):
        result = []

        def traverse_tree(node):
            # if left cheild exist, go left again and again
            if node.left:
                traverse_tree(node.left)

            # if right child exist, go right again and again
            if node.right:
                traverse_tree(node.right)

            # capture root node value
            result.append(node.value)

        traverse_tree(self.root)

        print(f"dfs_post_order: {result}")
        return result


    # breadth first order - level by level
    # uses queue
    def bfs(self):
        result = []
        queue = Queue()

        queue.enqueue(self.root)

        while len(queue) > 0:
            current_node = queue.dequeue()

            result.append(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)

            if current_node.right:
                queue.enqueue(current_node.right)

        print(f"bfs: {result}")
        return result


arr = []
cb = lambda x: arr.append(x)

bst = BST(15)
bst.insert(3)
bst.insert(36)
bst.insert(2)
bst.insert(12)
bst.insert(28)
bst.insert(39)

bst.size()
bst.contains(12) # True
bst.contains(37) # False
bst.min_value() # 2
bst.max_value() # 39
bst.for_each(cb) # [15, 3, 2, 12, 36, 28, 39]
bst.dfs_in_order() # [2, 3, 12, 15, 28, 36, 39]
bst.dfs_pre_order() # [15, 3, 2, 12, 36, 28, 39]
bst.dfs_post_order() # [2, 12, 3, 28, 39, 36, 15]
bst.bfs() # [15, 3, 2, 12, 36, 28, 39]

print(f"for_each: {arr}")

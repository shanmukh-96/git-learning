class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The Previous node doesn't exist in the list")
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_node(self, key):
        
        cur_node = self.head
        
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
            
        prev.next = cur_node.next
        cur_node.next = None
    
llist = LinkedList()
llist.append(1)
llist.append(5)
llist.prepend(7)
llist.delete_node(7)
llist.insert_after_node(llist.head.next, 8)
llist.print_list()

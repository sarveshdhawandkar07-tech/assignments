class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,insert_data):
        if not self.head:
            self.head = Node(insert_data,None)
            return
        itr = self.head
        while itr:
            if not itr.next:
                itr.next = Node(insert_data,None)
                return
            itr = itr.next
            
    def print_ll(self):
        if not self.head:
            print("Linked List is empty")
            return
        hashset = set()
        itr = self.head
        str_ll = ""
        while itr:
            str_ll += str(itr.data) + "-->"
            if itr in hashset:
                break
            else:
                hashset.add(itr)
            itr = itr.next
        print(str_ll)
    
    def make_circular(self):
        if not self.head:
            print("List is Empty")
            return
        itr = self.head
        while itr:
            if not itr.next:
                itr.next = self.head
                return
            itr = itr.next
    
    def get_length_circular(self):
        count = 0
        if not self.head:
            return count
        hashset = set()
        itr = self.head
        while itr:
            if itr in hashset:
                return count
            else:
                hashset.add(itr)
            count += 1
            itr = itr.next
    
    def connect_to_intermediate(self):
        if not self.head:
            print("List is Empty")
            return
        length = self.get_length_circular()
        middle = length//2 + 1
        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == middle:
                middle_node = itr 
            elif count == length:
                itr.next = middle_node
                return
            itr = itr.next
    
    def relinking(self):
        if not self.head:
            print("List is Empty")
            return 
        hashset = set()
        itr = self.head
        while itr:
            if itr.next in hashset:
                itr.next = self.head
                return
            else:
                hashset.add(itr)
            itr =  itr.next
                
    
            
ll = LinkedList()
ll.insert_at_end("A")
ll.insert_at_end("B")
ll.insert_at_end("C")
ll.insert_at_end("D")
ll.insert_at_end("E")
ll.print_ll()
ll.make_circular()
ll.print_ll()
print(ll.get_length_circular())
ll.connect_to_intermediate()
ll.print_ll()
ll.relinking()
ll.print_ll()

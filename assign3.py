class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,insert_data):
        new_node = Node(insert_data,None)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = new_node
        new_node.next = self.head
        return
            
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

    def distort(self,position):
        if self.head is None:
            return 
        last = self.head
        while last.next != self.head:
            last = last.next
        target = self.head
        count = 1
        while count < position:
            target = target.next
            count += 1
        last.next = target


    def relinking(self): # Brute Force
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

    def relinking_updated(self): #  Floyde's cycle finding algorithm
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return

        slow = self.head
        last = None
        while slow is not fast:
            slow = slow.next
            last = fast
            fast = fast.next

        if last is None:
            return
        last.next = self.head

    
            
ll = LinkedList()
ll.insert_at_end("A")
ll.insert_at_end("B")
ll.insert_at_end("C")
ll.insert_at_end("D")
ll.insert_at_end("E")
ll.print_ll()
ll.distort(3)
ll.print_ll()
ll.relinking_updated()
ll.print_ll()

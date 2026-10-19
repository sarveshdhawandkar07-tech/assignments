# Merge K linked lists
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

    def insert_array(self,arr):
        for value in arr:
            self.insert_at_end(value)
    
    def print_ll(self):
        if not self.head:
            print("Linked List is empty")
            return
        itr = self.head
        str_ll = ""
        while itr:
            str_ll += str(itr.data) + "-->"
            itr = itr.next
        print(str_ll)
            
    # first merge two lists
    def merge2lists(self,list1,list2):
        
        dummy = Node(0,None)
        itr = dummy
        
        while list1 and list2:
            
            if list1.data <= list2.data:
                itr.next = list1
                list1 = list1.next
            
            else:
                itr.next = list2
                list2 = list2.next
            
            itr = itr.next
        itr.next = list1 if list1 else list2
        return dummy.next
    
#     for merging k linked lists
    def merge_k_lists(self,lists):
        merged_head = self.merge2lists(lists[0],lists[1])
        for i in range(2,len(lists)):
            merged_head = self.merge2lists(merged_head,lists[i])
        return merged_head
        
    
ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()
ll4 = LinkedList()
mergedlist = LinkedList()
ll1.insert_array([5,6])
ll2.insert_array([7,8])
ll3.insert_array([1,2])
ll4.insert_array([9,10])
ll1.print_ll()
ll2.print_ll()
ll3.print_ll()
ll4.print_ll()
lists = [ll1.head,ll2.head,ll3.head,ll4.head]
mergedlist.head = mergedlist.merge_k_lists(lists)
mergedlist.print_ll()

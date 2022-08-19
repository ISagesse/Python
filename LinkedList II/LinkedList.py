class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        cur_head = self.head
        new_node.next = cur_head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next

        cur_node.next = new_node

    def print_data(self):
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + ' --> '
            cur = cur.next

        print()
        print(llstr)
        print()

    def get_length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def remove_by_index(self, index):
        if index >= self.get_length() or index < 0:
            print('ERROR: Index out of bounds')
            return
        
        if index == 0:
            cur = self.head
            self.head = cur.next
            return

        idx = 0
        cur = self.head
        while cur:
            if idx == index - 1:
                cur.next = cur.next.next
                break
            idx += 1
            cur = cur.next

    def insert_at(self, index, data):
        new_node = Node(data)
        if index >= self.get_length() or index < 0:
            print('ERROR: Index out of bounds')
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        idx = 0
        cur = self.head
        while cur:
            if idx == index - 1:
                prev = cur.next
                cur.next = new_node
                new_node.next = prev
                break
            idx += 1
            cur = cur.next                
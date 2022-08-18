

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head_node(self):
        return self.head_node.get_data()

    def remove_head(self):
        self.head_node = self.head_node.get_next_node()

    def add_to_beginning(self, data):
        new_node = Node(data)
        if self.head_node == None:
            self.head_node = new_node
        else:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head_node == None:
            self.head_node = new_node
            return
        else:
            cur = self.head_node
            while(cur.get_next_node() != None):
                cur = cur.get_next_node()
            cur.set_next_node(new_node)

    def read_all(self):
        data = ''

        if self.head_node != None:
            cur = self.head_node
            while(cur != None):
                data += str(cur.get_data()) + ' '
                cur = cur.get_next_node()

        return data

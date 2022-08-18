from list import LinkedList


ll = LinkedList()

ll.append(data=1)
ll.append(data=2)
ll.append(data=3)

ll.add_to_beginning(4)
ll.add_to_beginning(5)
ll.add_to_beginning(6)
print(ll.get_head_node())
ll.remove_head()
print(ll.get_head_node())

print(ll.read_all())
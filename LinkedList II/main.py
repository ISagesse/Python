from LinkedList import LinkedList

ll = LinkedList()

# append value
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# adding to the head / new head node
ll.insert_at_beginning(-4)
ll.insert_at_beginning(-3)
ll.insert_at_beginning(-2)
ll.insert_at_beginning(-1)
ll.append(5)
ll.print_data()

# getting the liked list length
#print(ll.get_length())

# remove value by index
ll.remove_by_index(6)

ll.print_data()

# insert data at a given index
ll.insert_at(3, -3.5)
ll.print_data()
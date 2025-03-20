from creating_reversing import Node, print_linked_list

# boshiga qo'shish

def add_to_head(head, value):
    new_node = Node(value=value)
    new_node.next = head
    return new_node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

add_to_head(node1, 4)

print_linked_list(add_to_head(node1, 4))

def add_to_tail(head, value):
    new_node = Node(value=value)
    if not head:
        return new_node
    
    current = head

    while current.next:
        current = current.next
    
    current.next = new_node
    return head

add_to_tail(node1, 5)

print_linked_list(add_to_head(node1, 5))

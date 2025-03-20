class Node:
    def __init__(self, value):
        self.value = value  # Ma'lumot
        self.next = None  # Keyingi node'ga pointer

    def print(self):
        while self:
            print(self.value, end=" -> ")
            self = self.next
        print("NULL")

    def reverse(self):
        print("REVERSING:")
        prev = None
        current = self

        while current:
            # print(current.value)
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            # prev.print()
        # prev.print()
        self = prev
        return prev


# Node yaratamiz
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Bog'lash
node1.next = node2
node2.next = node3

# Linked List boshi
# head = node1

# node1.print()
node1 = node1.reverse()
node1.print()
# print(node1.value)


def print_linked_list(head):
    while head:
        print(head.value, end=" → ")
        head = head.next
    print("NULL")

print_linked_list(node1)



def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Keyingi node'ni saqlaymiz
        current.next = prev  # Hozirgi node'ni oldingisiga bog'laymiz
        prev = current  # Prev'ni yangilaymiz
        current = next_node  # Keyingi node'ga o'tamiz

    return prev  # Yangi head qaytariladi

# Reverse qilamiz
new_head = reverse_linked_list(node1)
print_linked_list(new_head)  # Endi: 30 → 20 → 10 → NULL

# Doubly Linked List

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

Head = Tail = DoublyNode(1)

# Display the Doubly Linked List - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

#display(Head)

# Insert at beginning - O(n)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

Head, Tail = insert_at_beginning(Head, Tail, 3)
#display(Head)

# insert at the end - O(n)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=Tail)
    tail.next = new_node
    return head, new_node

Head, Tail = insert_at_end(Head, Tail, 2)
#print(Tail)
#display(Head)

# insert at specific position - O(n)
def insert_at_position(head, tail, pos, val):
    if pos == 0:
        return insert_at_beginning(head, tail, val)
    curr = head
    new_node = DoublyNode(val)
    
    for _ in range(pos-1):
        if curr is None:
            raise IndexError("Position out of bounds")
        curr = curr.next
    new_node.next = curr.next
    new_node.prev = curr
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    if new_node.next is None:
        tail = new_node
    return head, tail

Head, Tail = insert_at_position(Head, Tail, 2, 0)
# print(Head)
# display(Head)

# Delete from beginning - O(n)
def delete_from_beginning(head, tail):
    if head is None:
        return None, None
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head, tail

# Delete from end - O(n)
def delete_from_end(head, tail):
    if tail is None:
        return None, None
    new_tail = tail.prev
    if tail.prev:
        new_tail.next = None
    return head, new_tail

# Delete from specific position - O(n)
def delete_from_position(head, tail, pos):
    if pos == 0:
        return delete_from_beginning(head, tail)
    
    curr = head
    for _ in range(pos):
        if curr is None:
            raise IndexError("Position out of bounds")
        curr = curr.next
    if curr.prev:
        curr.prev.next = curr.next
    if curr.next:
        curr.next.prev = curr.prev
    if curr == tail:
        tail = curr.prev
    return head, tail

# Reverse the Doubly Linked List - Iterative - O(n)
def reverse_iterative(head, tail):
    curr = head
    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev
    return tail, head

# Reverse the Doubly Linked List - Recursive - O(n)
def reverse_recursive(node):
    if not node:
        return None
    node.prev, node.next = node.next, node.prev
    if not node.prev:
        return node
    return reverse_recursive(node.prev)
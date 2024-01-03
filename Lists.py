class ListNode:
    def __init__(self, data = None):
        self.next = None        
        self.value = data

def add_to_list(L1: ListNode, value = None):    
    current_node = L1
    while current_node.next:
        current_node = current_node.next
    current_node.next = ListNode(value)

def print_list(head: ListNode):
    print_me = []
    current_node = head
    while current_node:
        print_me.append(current_node.value)
        current_node = current_node.next
    print(print_me)
        
# P1: Merge two sorted lists
def p1_merge_two_sorted_lists(L1: ListNode,
                           L2: ListNode) -> ListNode:
    head = tail = ListNode()

    while L1 and L2:
        tail.next = ListNode()
        tail = tail.next
        if L1.value <= L2.value:
            tail.value, L1 = L1.value, L1.next
        elif L2.value < L1.value:
            tail.value, L2 = L2.value, L2.next
        
    tail.next = L1 or L2    
    return head.next
    
print("Part1. Merge two sorted list")
L1 = L1_head = ListNode(2)
add_to_list(L1, 5)
add_to_list(L1, 7)

L2 = L2_head = ListNode(3)
add_to_list(L2, 11)

print("L1 and L2 are: ")
print_list(L1_head)
print_list(L2_head)

L3 = p1_merge_two_sorted_lists(L1_head, L2_head)
print("Merged List:")
print_list(L3)

# P2: Accept a list and reverse sublist from s to f, inclusive
# Index starts at 1

def p2_reverse_list(L1: ListNode, start: int, finish: int) -> ListNode:
    head = tail = L1

    # Identify where start is
    for x in range(start):
        anchor = tail
        tail = tail.next

    ''' SCRATCHPAD: searching for a pattern
    tail = end = new.next
    tail.next = end - 1 = new = new1.next
    tail.next.next = end - 2 = new1 = new2.next
    tail.next.next.next = end - 3 = new2 
    '''
    
    temp = None
    new = ListNode(0)
    for _ in range(finish - start):
        if temp:
            new = ListNode(0)
            new.next = temp
        else:
            new.next = ListNode(tail.value)
        new.value, temp, tail = tail.next.value, new, tail.next
    
    return temp
            
L1 = L1_head = ListNode(11)
add_to_list(L1, 3)
add_to_list(L1, 5)
add_to_list(L1, 7)
add_to_list(L1, 2)

print("\nPart2. Reverse sublist for below: ")
print_list(L1)
print("Reversed list below:")
print_list(p2_reverse_list(L1, 1, 3))
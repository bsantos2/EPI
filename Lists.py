class ListNode:
    def __init__(self, data = None, next = None):
        self.next = next        
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
    
L1 = L1_head = ListNode(2)
add_to_list(L1, 5)
add_to_list(L1, 7)

L2 = L2_head = ListNode(3)
add_to_list(L2, 11)

print_list(L1_head)
print_list(L2_head)

L3 = p1_merge_two_sorted_lists(L1_head, L2_head)
print_list(L3)
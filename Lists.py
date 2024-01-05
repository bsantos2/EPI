# Suggested Chapter 7 Problems
# 1, 2, 3, 4, 7, 10, 11
class ListNode:
    def __init__(self, data = None):
        self.next = None        
        self.value = data

def add_to_list(L1: ListNode, value = None):    
    current_node = L1
    while current_node.next:
        current_node = current_node.next
    current_node.next = ListNode(value)

def add_list_to_list(L1:ListNode, L2: ListNode):
    current_node = L1
    while current_node.next:
        current_node = current_node.next
    current_node.next = L2    

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

# P3: Check if linked list has a cycle
# My own approoach uses extra storage but EPI calls for no storage. 
# I dont know how to do that
def p3_has_cycle(L1: ListNode) -> ListNode:
    bank = set()    # Use hashset instead of dict[] because two different nodes can have same value
    current_node = L1
    while current_node:
        if current_node in bank:
            return current_node
        else:
            bank.add(current_node)
            current_node = current_node.next
    return current_node

# Common approach suggested using slow/fast pointers from Floyd's Tortoise and Hare Algo
def p3_has_cycle_rabbit_tortoise_pointers(L1: ListNode) -> ListNode:
    slow = L1
    fast = slow.next.next

    while fast and fast.next:
        if slow == fast:
            return slow
        else:
            fast = fast.next.next
            slow = slow.next
    return None

L1 = L1_head = ListNode(11)
add_to_list(L1, 3)
add_to_list(L1, 5)
add_to_list(L1, 7)
add_to_list(L1, 2)
print("\nPart3. Check if linked list has a cycle")
print_list(L1)
assert p3_has_cycle(L1) is None, f"L1 currently has no cycles. Recheck p3_has_cycle."
assert p3_has_cycle_rabbit_tortoise_pointers(L1) is None, f"L1 currently has no cycles. Recheck p3_has_cycle."
add_list_to_list(L1, L1_head)
assert p3_has_cycle(L1) is not None, f"L1 currently has a loop. However p3_has_cycle detected no loops."
assert p3_has_cycle_rabbit_tortoise_pointers(L1) is not None,f"L1 currently has a loop. However p3_has_cycle detected no loops."

# P4: Check if two lists have any overlap

# My approach involved nested loops, but it's inefficient in time at O(n^2)
# Not good
def p4_no_overlapping_list(L1: ListNode, L2: ListNode) -> ListNode:
    while L1:
        while L2:
            if L1 == L2:
                return L1
            else:
                L2 = L2.next
        L1 = L1.next

    return None

def p4_optimized_no_overlapping_list(L1: ListNode, L2: ListNode) -> ListNode:
    return

L1 = L1_head = ListNode(11)
add_to_list(L1, 3)
add_to_list(L1, 5)
add_to_list(L1, 7)
add_to_list(L1, 2)

L2 = L2_head = ListNode(9)
add_to_list(L2, 1)

assert p4_no_overlapping_list(L1_head, L2_head) is None, f"The function detects overlap when there isn't any."
add_list_to_list(L2, L1_head) # coerce overlap
assert p4_no_overlapping_list(L1_head, L2_head) is not None, f"The function detects no overlap when we expect it."
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    # cur = head
    # prev = None
    # while cur:
    #     if cur.val == val and cur == head:
    #         head = head.next
    #     elif cur.val == val:
    #         prev.next = cur.next
    #         cur = prev
    #
    #     prev = cur
    #     cur = cur.next
    #
    # return head


    #or

    fake = ListNode(-1)
    fake.next = head
    curr = fake
    # Loop till curr.next not null...
    while curr.next:
        # if we find the target val same as the value of curr.next...
        if curr.next.val == val:
            # Skip that value and keep updating curr...
            curr.next = curr.next.next
        # Otherwise, move curr forward...
        else:
            curr = curr.next
    # Return the linked list...
    return fake.next


head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(2)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

head = remove_elements(head, 2)

while head:
    print(head.val)
    head = head.next
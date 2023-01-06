class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    cur = head

    while cur.next:

        newNode = ListNode(cur.next.val, head)
        head = newNode
        cur.next = cur.next.next

    return head


head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

head = reverse_linked_list(head)

while head:
    print(head.val)
    head = head.next


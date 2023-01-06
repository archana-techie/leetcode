class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def palindrome_linked_list(head):
    sp = head
    fp = head.next

    while fp and fp.next:
        sp = sp.next
        fp = fp.next.next

    cur = sp
    end = sp
    while cur.next:
        new = ListNode(cur.next.val, end)
        end = new
        cur.next = cur.next.next

    while head and end:
        if head.val != end.val:
            return False
        head, end = head.next, end.next

    return True


head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(2)
l3 = ListNode(4)

head.next = l1
l1.next = l2
l2.next = l3

print("----------------------")

print(palindrome_linked_list(head))



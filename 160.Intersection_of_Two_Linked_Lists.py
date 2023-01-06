class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    l1, l2 = headA, headB

    while l1 != l2:
        l1 = headB if not l1 else l1.next
        l2 = headA if not l2 else l2.next

    return l2



ha = ListNode(1)
ha1 = ListNode(2)
ha2 = ListNode(3)

hb = ListNode(2)
hb1 = ListNode(2)
hb2 = ListNode(2)
hb3 = ListNode(4)
hb4 = ListNode(5)
hb5 = ListNode(6)

ha.next = ha1
ha1.next = ha2
ha2.next = hb3
hb3.next = hb4
hb4.next = hb5

hb.next = hb1
hb1.next = hb2
hb2.next = hb3


print(getIntersectionNode(ha, hb).val)

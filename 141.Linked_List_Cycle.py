class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    data = set()
    while head.next:
        if head.next.val in data:
            return "True"
        else:
            data.add(head.val)
        head = head.next
    return "False"

    # or

    # s = head
    # f = head
    #
    # while f and f.next:
    #     s = s.next
    #     f = f.next.next
    #
    #     if s == f:
    #         return True
    # return False



h = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)

h.next = l1
l1.next = l2
l2.next = l1

print(hasCycle(h))
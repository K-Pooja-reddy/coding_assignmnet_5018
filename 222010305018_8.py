class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
def getIntersectionNode(headA, headB):
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return lengt
    lenA, lenB = get_length(headA), get_length(headB)
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None
a1 = ListNode('a1')
a2 = ListNode('a2')
c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')
b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')
a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1
intersection_node = getIntersectionNode(a1, b1)
print("Intersection Node:", intersection_node.val if intersection_node else None)
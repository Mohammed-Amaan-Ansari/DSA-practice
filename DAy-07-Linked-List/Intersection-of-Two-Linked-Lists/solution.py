class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    a = headA
    b = headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


if __name__ == "__main__":
    # Shared intersection part
    common = ListNode(8, ListNode(4, ListNode(5)))

    # List A
    headA = ListNode(4, ListNode(1, common))

    # List B
    headB = ListNode(5, ListNode(6, ListNode(1, common)))

    result = get_intersection_node(headA, headB)
    print(result.val if result else None)  # 8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):

    dummy = ListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


# Helper function
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Test Cases
if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    updated = remove_nth_from_end(head, 2)

    print_list(updated)
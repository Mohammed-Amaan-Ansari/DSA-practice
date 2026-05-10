class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


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

    reversed_head = reverse_list(head)

    print_list(reversed_head)
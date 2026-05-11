class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Compare first and second half
    left = head
    right = prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(is_palindrome(head1))  # True

    head2 = ListNode(1, ListNode(2))
    print(is_palindrome(head2))  # False
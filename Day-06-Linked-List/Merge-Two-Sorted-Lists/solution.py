class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):

    dummy = ListNode()
    tail = dummy

    while list1 and list2:

        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1:
        tail.next = list1

    if list2:
        tail.next = list2

    return dummy.next


# Helper function
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Test Cases
if __name__ == "__main__":

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    merged = merge_two_lists(l1, l2)

    print_list(merged)
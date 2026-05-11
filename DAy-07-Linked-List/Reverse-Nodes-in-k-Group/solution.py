class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth_node(group_prev, k)
        if not kth:
            break

        group_next = kth.next

        # reverse group
        prev = group_next
        curr = group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

    return dummy.next


def get_kth_node(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = reverse_k_group(head, 2)
    print_list(result)  # 2 -> 1 -> 4 -> 3 -> 5 -> None
from common.linked_list import linked_list
from common.linked_list import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return (l1 if l2 is None else l2)

        main_list_pointer = l1 if l1.val < l2.val else l2
        other_list_pointer = l2 if main_list_pointer is l1 else l1
        head = main_list_pointer

        while main_list_pointer.next and main_list_pointer.next.val < other_list_pointer.val:
            main_list_pointer = main_list_pointer.next

        merge_pointer = main_list_pointer.next
        main_list_pointer.next = other_list_pointer

        while other_list_pointer.next and merge_pointer and \
                other_list_pointer.next.val <= merge_pointer.val:
            other_list_pointer = other_list_pointer.next
        other_list_new_head = other_list_pointer.next
        other_list_pointer.next = merge_pointer
        self.mergeTwoLists(other_list_new_head, head)

        return head


if __name__ == '__main__':
    print(Solution().mergeTwoLists(linked_list([1, 2, 4]), linked_list([1, 3, 4])))

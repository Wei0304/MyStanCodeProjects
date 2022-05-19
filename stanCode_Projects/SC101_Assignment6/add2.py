"""
File: add2.py
Name: Wei
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    is_first = True  # switcher for first round
    cur_1 = l1
    cur_2 = l2
    carry = 0  # to carry the digit based on decimal

    while cur_1 and cur_2 is not None:
        #  in condition that need to carry decimal to the next digit
        if cur_1.val + cur_2.val > 9:
            if is_first:
                ans = ListNode(cur_1.val + cur_2.val-10, None)
                is_first = False
                ans_cur = ans
                carry = 1
                cur_1 = cur_1.next
                cur_2 = cur_2.next
            else:
                ans_cur.next = ListNode(cur_1.val + cur_2.val-10+carry, None)
                carry = 1
                ans_cur = ans_cur.next
                cur_1 = cur_1.next
                cur_2 = cur_2.next
        #  in condition that don't need to carry decimal to the next digit
        else:
            if is_first:
                ans = ListNode(cur_1.val + cur_2.val+carry, None)
                is_first = False
                carry = 0
                ans_cur = ans
                cur_1 = cur_1.next
                cur_2 = cur_2.next
            else:
                ans_cur.next = ListNode(cur_1.val + cur_2.val+carry, None)
                carry = 0
                ans_cur = ans_cur.next
                cur_1 = cur_1.next
                cur_2 = cur_2.next

    # In condition that the number of digits is different for l1 and l2
    while cur_1 or cur_2 is not None:
        #  if l1's number of digit is longer than l2
        if cur_1 is not None:
            if cur_1.val + carry > 9:
                ans_cur.next = ListNode(cur_1.val + carry-10, None)
                carry = 1
                ans_cur = ans_cur.next
                cur_1 = cur_1.next
            else:
                ans_cur.next = ListNode(cur_1.val + carry-10, None)
                carry = 0
                ans_cur = ans_cur.next
                cur_1 = cur_1.next
        #  if l2's number of digit is longer than l1
        else:
            if cur_2.val + carry > 9:
                ans_cur.next = ListNode(cur_2.val + carry, None)
                carry = 1
                ans_cur = ans_cur.next
                cur_2 = cur_2.next
            else:
                ans_cur.next = ListNode(cur_2.val + carry, None)
                carry = 0
                ans_cur = ans_cur.next
                cur_1 = cur_2.next

    #  In condition that the ans is having longest digit after carrying
    if carry != 0:
        ans_cur.next = ListNode(carry, None)

    return ans



####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()

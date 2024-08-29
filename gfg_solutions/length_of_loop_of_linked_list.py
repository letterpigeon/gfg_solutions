"""
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
"""

class FindLengthOfLoop:
    def find_length_of_loop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return 0
        count = 1
        slow = slow.next
        while slow != fast:
            count += 1
            slow = slow.next
        return count

import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestFindLengthOfLoop(unittest.TestCase):
    def test_no_loop(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        finder = FindLengthOfLoop()
        self.assertEqual(finder.find_length_of_loop(head), 0)

    def test_single_node_no_loop(self):
        head = ListNode(1)
        finder = FindLengthOfLoop()
        self.assertEqual(finder.find_length_of_loop(head), 0)

    def test_single_node_with_loop(self):
        head = ListNode(1)
        head.next = head
        finder = FindLengthOfLoop()
        self.assertEqual(finder.find_length_of_loop(head), 1)

    def test_multiple_nodes_with_loop(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head.next
        finder = FindLengthOfLoop()
        self.assertEqual(finder.find_length_of_loop(head), 3)

    def test_multiple_nodes_with_longer_loop(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = head.next.next
        finder = FindLengthOfLoop()
        self.assertEqual(finder.find_length_of_loop(head), 3)

if __name__ == '__main__':
    unittest.main()
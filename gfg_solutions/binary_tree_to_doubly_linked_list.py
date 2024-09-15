"""
Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeToDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def tree_to_dll(self, root: Node) -> Node:
        """
        Convert the binary tree to doubly linked list in place.  The returned node points to the head of the doubly
        linked list.  The original tree is modified in place, but can still be used as a binary tree.
        :param root: root of the binary tree
        :return: head of the converted doubly linked list
        """
        def inorder_convert(node: Node) -> None:
            if not node:
                return
            inorder_convert(node.left)
            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node

            self.prev = node
            inorder_convert(node.right)

        inorder_convert(root)
        return self.head

import unittest

class TestBinaryTreeToDoublyLinkedList(unittest.TestCase):
    def test_single_node_tree(self):
        root = Node(1)
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(root)
        self.assertEqual(head.val, 1)
        self.assertIsNone(head.left)
        self.assertIsNone(head.right)

    def test_left_skewed_tree(self):
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(root)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.right.val, 2)
        self.assertEqual(head.right.right.val, 3)

    def test_right_skewed_tree(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(root)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.right.val, 2)
        self.assertEqual(head.right.right.val, 3)

    def test_complete_binary_tree(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(root)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.right.val, 2)
        self.assertEqual(head.right.right.val, 3)

    def test_empty_tree(self):
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(None)
        self.assertIsNone(head)

    def test_complex_tree(self):
        root = Node(10)
        root.left = Node(12)
        root.right = Node(15)
        root.left.left = Node(25)
        root.left.right = Node(30)
        root.right.left = Node(36)
        bttdll = BinaryTreeToDoublyLinkedList()
        head = bttdll.tree_to_dll(root)
        self.assertEqual(head.val, 25)
        self.assertEqual(head.right.val, 12)
        self.assertEqual(head.right.right.val, 30)
        self.assertEqual(head.right.right.right.val, 10)
        self.assertEqual(head.right.right.right.right.val, 36)
        self.assertEqual(head.right.right.right.right.right.val, 15)
#!/usr/bin/python3
""" class Node that defines a node of a singly linked list """


class Node:
    def __init__(self, data, next_node=None):

        """Initialize a new Node.
            Args:
                data (int): The data of the node of a singly linked list.
                next_node (Node): The next_node of the node of a sll.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node


""" class that defines a singly linked list  """


class SinglyLinkedList:
    """ class that defines a singly linked list  """

    def __init__(self):
        self.head = None

    def sorted_insert(self, data):
        """ insert new Node in the Singly Linked List """

        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None and curr.next_node.data < data:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """ Print the Singly Linked List """
        current = self.head
        result = ""
        while current:
            result += str(current.data) + '\n'
            current = current.next_node
        return (result.rstrip())

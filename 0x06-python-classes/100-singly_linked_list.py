#!/usr/bin/python3
""" class Node that defines a node of a singly linked list """


class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node of a singly linked list.

        Returns:
            int: The data of the node of a singly linked list.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the the data part of the node of a singly linked list.

        Args:
            value (int): The data part of the node of a singly linked list.

        Raises:
            TypeError: data must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next_node of a singly linked list.

        Returns:
            Node: The next node of a singly linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set the the next_node of a singly linked list.

        Args:
            value (Node): The next_node of a singly linked list.

        Raises:
            TypeError: next_node must be a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.data) + '\n'
            current = current.next_node
        return (result.rstrip())

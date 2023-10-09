# Directory : 0x0A-python-inheritance

This directory contains Python scripts and modules related to the concept of inheritance in object-oriented programming (OOP) using Python. Inheritance is a fundamental concept in OOP that allows you to create new classes (child classes) based on existing classes (parent classes). It enables code reuse and the creation of hierarchical relationships between classes.

## Contents

0-lookup.py
A Python function that returns the list of available attributes and methods of an object.

1-my_list.py
A Python class MyList that inherits from the built-in list class. It adds a new method print_sorted() that prints the list in ascending order.

2-is_same_class.py
A Python function is_same_class(obj, a_class) that checks if an object obj is an instance of a given class a_class.

3-is_kind_of_class.py
A Python function is_kind_of_class(obj, a_class) that checks if an object obj is an instance of a class that inherits from a_class.

4-inherits_from.py
A Python function inherits_from(obj, a_class) that checks if an object obj inherits from a class a_class, using isinstance().

5-base_geometry.py
An abstract base class BaseGeometry that defines two abstract methods: area() and integer_validator(). It serves as a base class for geometry-related classes.

6-base_geometry.py
An updated version of BaseGeometry with added validation for the values passed to integer_validator().

7-base_geometry.py
An enhanced BaseGeometry class that includes a __str__() method to define a string representation of the object.
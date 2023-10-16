#!/usr/bin/python3
""" import json module """

import json
import turtle
""" Base calss """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.
            Args:
                id (int): id of the new instance
        """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        l_o = "[]"
        filename = str(cls.__name__) + ".json"
        if list_objs is not None:
            l_o = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        with open(filename, 'w') as f:
            f.write(l_o)

    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        """
        str_list = []
        if json_string is not None and len(json_string) > 0:
            str_list = json.loads(json_string)
        return (str_list)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances from file """
        filename = str(cls.__name__) + ".json"
        dict_list = []
        try:
            with open(filename, 'r') as file:
                data_str = file.read()
                str_list = cls.from_json_string(data_str)
                for dict in str_list:
                    dict_list.append(cls.create(**dict))
                return (dict_list)
        except FileNotFoundError:
            return dict_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw rectangle and square """
        screen = turtle.Screen()
        screen.title("Draw Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(1)
        for rect in list_rectangles:
            pen.penup()
            pen.goto(-rect.width / 2, -rect.height / 2)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(-square.side_length / 2, -square.side_length / 2)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.side_length)
                pen.left(90)

        screen.exitonclick()

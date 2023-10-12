#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
""" TestClassRecatngle """


class TestClassRectangle(unittest.TestCase):
    """ TestClassRectangle """
    
    def test_width(self):
        Base._Base__nb_objects = 0
        """ test_width """
        r1 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)

    def test_width_height(self):
        """ test_id_10 """
        self.assertEqual(Rectangle(10, 12).id, 2)
        self.assertEqual(Rectangle(0, 12).width, 0)
        self.assertEqual(Rectangle(10, 12).height, 12)
        self.assertEqual(Rectangle(8, 6).width + Rectangle(5, 1).height, 9)

    def test_x(self):
        Base._Base__nb_objects = 0
        """ test_x """
        r1 = Rectangle(10, 2, 15, 0, 12)
        self.assertEqual(r1.x, 15)

    def test_y(self):
        """ test_y """
        r1 = Rectangle(10, 2, 15, 2, 12)
        self.assertEqual(r1.y, 2)


    def test_Raise_ValueError_width(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError):
            Rectangle(-3, 2, 0, 0, 12)

    def test_Raise_ValueError_height(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError):
            Rectangle(10, -2, 0, 0, 12)
  
    def test_Raise_ValueError_x(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -5, 0, 12)

    def test_Raise_ValueError_y(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 5, -100, 12)

    def test_Raise_TypeError_width(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 0, 0, 12)

    def test_Raise_TypeError_height(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError):
            Rectangle(10, "2", 0, 0, 12)
  
    def test_Raise_TypeError_x(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "80", 0, 12)

    def test_Raise_TypeError_y(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "0", 12)

    def test_Area(self):
        """ test_Area """
        r = Rectangle(10, 2, 5, 0, 12)
        self.assertEqual(r.area(), 20)

    def test_Area_Zero(self):
        """ test_Area_Zero """
        r = Rectangle(10, 0)
        self.assertEqual(r.area(), 0)

    def test_Dispaly_2X2(self):
        """ test_Area_Zero """
        r = Rectangle(2, 2)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
            output = printed.getvalue()
        expected_output = "##\n##\n"
        self.assertEqual(output, expected_output)


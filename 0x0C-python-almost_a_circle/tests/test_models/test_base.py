#!/usr/bin/python3
import unittest
from models.base import Base
""" TestClassBase """


class TestClassBase(unittest.TestCase):
    """ TestClassBase """
    
    def test_id_10(self):
        """ test_id_10 """
        self.assertEqual(Base(10).id, 10)

    def test_id(self):
        """ test_id """
        self.assertEqual(Base().id, 1)

    def test_id_2(self):
        """ test_id_2 """
        self.assertEqual(Base().id, 2)

    def test_id_neg(self):
        """ test_id_neg """
        self.assertEqual(Base(-2).id, -2)
        
    def test_id_None(self):
        """ test_id_None """
        self.assertEqual(Base(None).id, 3)

    def test_id_Var(self):
        """ test_id_Var """
        r1 = Base(100)
        self.assertEqual(r1.id, 100)

    @unittest.expectedFailure
    def test_Raise_Failure(self):
        """ test_Raise_Failure """
        id = "100"
        with self.assertRaises(TypeError):
          Base(id)

    @unittest.expectedFailure
    def test_id_Failure(self):
        """  test_id_Failure"""
        self.assertEqual(Base(15).id, 100)

    def test_id_List(self):
        """ test_id_List """
        my_list = [10, 11, 12]
        self.assertEqual(Base(my_list).id, [10, 11, 12])

    def test_id_Str(self):
        """ test_id_Str """
        self.assertEqual(Base("hi").id, "hi")

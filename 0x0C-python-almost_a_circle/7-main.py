#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    r2 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(None, 2, 3, 4)
    print(r1)

    
    r2.update(None, 2, 3, 4, 5, 6), print(r2)
    r2.update(None, 2, 3, 4, 5, 6) , print(r2)
    r2.update(None, 2, 3, 4, 5, 6) , print(r2)
  

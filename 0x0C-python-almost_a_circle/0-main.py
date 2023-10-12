#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
    
    b6 = Base(12)
    print(b6.id)
    print(b4.id)
    
    my_list = ["10", 11, 12]
    print(Base(my_list).id)
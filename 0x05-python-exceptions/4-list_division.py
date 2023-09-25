#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for x in range(list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError):
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            res_list.append(div)
    return (res_list)

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            i += 1
    return new_list

#!/usr/bin/python3

def list_division(list_1, list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            res = list_1[i] / list_2[i]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except (ValueError, TypeError):
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
    return new_list

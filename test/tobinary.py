# -*- coding: utf-8 -*-


def tobinary(num, binary_list=None):
    if binary_list is None:
        binary_list = []

    if num == 0:
        return 0

    binary_list.insert(0, num % 2)

    if num // 2 == 0:
        return binary_list

    return tobinary(num // 2, binary_list)


print(tobinary(7))

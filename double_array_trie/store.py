# -*- coding: utf-8 -*-


class IntegerArrayList(object):
    def __init__(self, initial_capacity=16, inc_ratio_nom=1, inc_ratio_denom=1, fixed_inc=1000):
        if initial_capacity < 0:
            raise Exception("Negative capacity specified %d" % initial_capacity)
        self.__data = []
        self.__INCREASE_RATIO_NUMERATOR = inc_ratio_nom
        self.__INCREASE_RATIO_DENOMINATOR = inc_ratio_denom
        self.__FIXED_INCREASE = fixed_inc
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __check_valid_index(self, index):
        if index > self.__size:
            raise Exception("Index: " + str(index) + ", Size: " + str(self.__size))


class DoubleIntegerArray(object):
    def __init__(self, initial_capacity):
        self.__first = IntegerArrayList(initial_capacity)

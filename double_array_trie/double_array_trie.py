# -*- coding: utf-8 -*-
from double_array_trie.abstract_double_array_trie import AbstractDoubleArrayTrie
from data_structure.treeset import TreeSet


class DoubleArrayTrie(AbstractDoubleArrayTrie):
    def __init__(self, alphabet_length):
        super().__init__(alphabet_length)
        self.__base = []
        self.__check = []
        self.__base.append(super()._INITIAL_ROOT_BASE)
        self.__check.append(super()._ROOT_CHECK_VALUE)
        self.__free_positions = TreeSet

    def _ensure_reachable_index(self, index):
        while super()._get_size() < index:
            self.__base.append(super()._EMPTY_VALUE)
            self.__check.append(super()._EMPTY_VALUE)
            self.__free_positions.add(len(self.__base)-1)

    def _next_available_hop(self, for_value):
        while self.__free_positions.ceiling(for_value) >= for_value:
            self._ensure_reachable_index(len(self.__base) + 1)

        result = self.__free_positions.ceiling(for_value) - for_value

        return result

    def _next_available_move(self, values):
        if len(values) == 1:
            return self._next_available_hop(values[0])

        minValue = values[0]
        maxValue = values[len(values)-1]

        neededPositions = maxValue - minValue + 1
        possible = self.__find_consecutive_free(neededPositions)
        if possible - minValue >= 0:
            return possible - minValue

        self._ensure_reachable_index(len(self.__base) + neededPositions)
        return len(self.__base) - neededPositions - minValue

    def __find_consecutive_free(self, amount):
        if self.__free_positions.__len__() == 0:
            return -1
        it = self.__free_positions.__iter__()
        from_value = it[0]
        previous = from_value

        consecutive = 1
        i = 1
        while consecutive < amount and i < len(it):
            current = it[i]
            if current - previous == 1:
                previous = current
                consecutive = consecutive + 1
            else:
                from_value = current
                previous = from_value
                consecutive = 1
        if consecutive == amount:
            return from_value
        else:
            return -1

    def _get_base(self, position):
        return self.__base[position]

    def _get_check(self, position):
        return self.__check[position]

    def _set_base(self, position, value):
        self.__base[position] = value
        if value == super()._EMPTY_VALUE:
            self.__free_positions.add(position)
        else:
            self.__free_positions.remove(position)

    def _set_check(self, position, value):
        self.__check[position] = value
        if value == super()._EMPTY_VALUE:
            self.__free_positions.add(position)
        else:
            self.__free_positions.remove(position)

    def _get_size(self):
        return len(self.__base)

    def _update_search(self, state, string_index, values):
        pass

    def _update_insert(self, state, string_index, values):
        pass

    def _update_child_move(self, parent_index, for_character, new_parent_base):
        pass

    def _update_state_move(self, state_index, new_base):
        pass






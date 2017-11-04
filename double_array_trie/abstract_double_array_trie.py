# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from data_structure.treeset import TreeSet
from enum import Enum


class AbstractDoubleArrayTrie(metaclass=ABCMeta):
    def __init__(self, alphabet_length):
        # The leaf base value
        self._LEAF_BASE_VALUE = -2
        # The root check value, normally unnecessary
        self._ROOT_CHECK_VALUE = -3
        # The unoccupied spot value
        self._EMPTY_VALUE = -1
        # The initial offset.
        self._INITIAL_ROOT_BASE = 1
        # The alphabet length
        self.__alphabet_length = alphabet_length

    def add_to_trie(self, values):
        changed = False
        state = 0
        len_list = len(values)

        for i in range(len_list):
            c = values[i]
            transition = self._get_base(state) + c
            self._ensure_reachable_index(transition)
            if self._get_check(transition) == self._EMPTY_VALUE:
                self._set_check(transition, state)
                if i == len_list - 1 :
                    self._set_base(transition, self._LEAF_BASE_VALUE )
                    changed = True
                else:
                    self._set_base(transition, self._next_available_hop(values[i + 1]))
                    changed = True
            elif self._get_check(transition) != state:
                self._resolve_conflict(state, c)
                changed = True
                continue

            self._update_insert(state, i - 1, list)
            state = transition

        return changed

    def _resolve_conflict(self, s, new_value):
        values = TreeSet()
        values.add(new_value)
        for c in range(self.__alphabet_length):
            temp_next = self._get_base(s) + c
            if temp_next < self._get_size() and self._get_check(temp_next) == s:
                values.add(c)
        new_location = self._next_available_move(values)
        values.remove(new_value)
        for c in values:
            temp_next = self._get_base(s) + c
            self._set_check(new_location + c, s)
            self._set_base(new_location + c, self._get_base(self._get_base(s) + c))
            self._update_child_move(s, c, new_location)
            if self._get_base(self._get_base(s) + c) != self._LEAF_BASE_VALUE:
                for d in range(self.__alphabet_length):
                    temp_next_child = self._get_base(self._get_base(s) + c) + d
                    if temp_next_child < self._get_size() and self._get_check(temp_next_child) == self._get_base(s) + c:
                        self._set_check(self._get_base(self._get_base(s) + c) + d, new_location + c)
                    elif temp_next_child >= self._get_size():
                        break
                self._get_base(self._get_base(s) + c, self._EMPTY_VALUE)
                self._set_check(self._get_base(s) + c, self.EMPTY_VALUE)

        self._set_base(s, new_location)
        self._update_state_move(s, new_location)

    def contains_prefix(self, prefix):
        return self._run_prefix(prefix)

    def _run_prefix(self, prefix):
        state = 0
        i = 0
        result = SearchState()
        result.prefix = prefix
        result.result = SearchResult.PURE_PREFIX
        while i < len(prefix):
            current = prefix[i]
            transition = self._get_base(state) + current
            if transition < self._get_size() and self._get_check(transition) == state:
                if self._get_base(transition) == self._LEAF_BASE_VALUE:
                    if i == len(prefix) - 1:
                        result.result = SearchResult.PERFECT_MATCH
                        break
                    else:
                        result.result = SearchResult.NOT_FOUND
                        break

                state = transition
            else:
                result.result = SearchResult.NOT_FOUND
                break
            self._update_search(state, i, prefix)
            i = i + 1
        self._update_search(state, i, prefix)
        result.finishedAtState = state
        result.index = i

        return result

    def get_alphabet_size(self):
        return self.__alphabet_length

    @abstractmethod
    def _get_base(self, position):
        pass

    @abstractmethod
    def _ensure_reachable_index(self, index):
        pass

    # Returns the value of the check array at <tt>position</tt>.
    @abstractmethod
    def _get_check(self, position):
        pass

    @abstractmethod
    def _set_check(self, position, value):
        pass

    @abstractmethod
    def _set_base(self, position, value):
        pass

    @abstractmethod
    def _next_available_hop(self, for_value):
        pass

    @abstractmethod
    def _update_insert(self, state, string_index, values):
        pass

    @abstractmethod
    def _get_size(self):
        pass

    @abstractmethod
    def _next_available_move(self, values):
        pass

    @abstractmethod
    def _update_child_move(self, parent_index, for_character, new_parent_base):
        pass

    @abstractmethod
    def _update_state_move(self, state_index, new_base):
        pass

    @abstractmethod
    def _update_search(self, state, string_index, values):
        pass


class SearchState(object):
    prefix = []
    index = 0
    finishedAtState = None
    result = SearchResult.PERFECT_MATCH


class SearchResult(Enum):
    PERFECT_MATCH = 1
    PURE_PREFIX = 2
    PREFIX = 3
    NOT_FOUND = 4








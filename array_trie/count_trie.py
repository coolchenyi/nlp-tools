# -*- coding: utf-8 -*-

from array_trie.double_array_trie import DoubleArrayTrie


class CountingTrie(DoubleArrayTrie):
    def __init__(self, alphabet_length):
        super().__init__(alphabet_length)
        self.__exist_counts = [0]
        self.__search_counts = [0]

    def _ensure_reachable_index(self, limit):
        super()._ensure_reachable_index(limit)
        while len(self.__exist_counts) <= limit:
            self.__exist_counts.append(0)

        while len(self.__search_counts) <= limit:
            self.__search_counts.append(0)

    def _update_child_move(self, parent_index, for_character, new_parent_base):
        super()._update_child_move(parent_index, for_character, new_parent_base)
        old_count = self.__exist_counts[self._get_base(parent_index) + for_character]
        self.__exist_counts[new_parent_base + for_character] = old_count
        self.__exist_counts[self._get_base(parent_index) + for_character] = 0

        old_count = self.__search_counts[self._get_base(parent_index) + for_character]
        self.__search_counts[new_parent_base + for_character] = old_count
        self.__search_counts[self._get_base(parent_index) + for_character] = 0

    def _update_insert(self, state, string_index, values):
        super()._update_insert(state, string_index, values)
        self.__exist_counts[state] = self.__exist_counts[state] + 1

    def _update_search(self, state, string_index, values):
        super()._update_search(state, string_index, values)
        if string_index == len(values) - 1:
            self.__search_counts[state] = self.__search_counts[state] + 1

    def get_search_count_for(self, prefix):
        state = self._run_prefix(prefix)
        if state.index == len(prefix) - 1:
            return self.__search_counts[state.finishedAtState]
        else:
            return 0

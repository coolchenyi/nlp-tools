# -*- coding: utf-8 -*-
import random
from array_trie.double_array_trie import DoubleArrayTrie
from array_trie.abstract_double_array_trie import SearchResult
from array_trie.count_trie import CountingTrie
import unittest


class TestDoubleArrayTrie(unittest.TestCase):
    # def test_robustness_under_stress(self):
    #     ALPHABET_SIZE = 120
    #     NUMBER_OF_STRINGS = 10000
    #     MAXIMUM_STRING_SIZE = 100
    #
    #     data = []
    #     trie = DoubleArrayTrie(ALPHABET_SIZE)
    #
    #     for i in range(NUMBER_OF_STRINGS):
    #         to_add = []
    #         for j in range(MAXIMUM_STRING_SIZE):
    #             to_add.append(random.randint(1, ALPHABET_SIZE))
    #
    #         data.append(to_add)
    #
    #     for list_data in data:
    #         self.assertTrue(trie.add_to_trie(list_data))
    #         self.assertFalse(trie.add_to_trie(list_data))
    #
    #     for list_data in data:
    #         self.assertEqual(SearchResult.PERFECT_MATCH, trie.contains_prefix(list_data))
    #
    #     for list_data in data:
    #         remove_size = random.randint(0, len(list_data)) + 1
    #
    #         for i in range(remove_size):
    #             list_data.remove(len(list_data) - 1)
    #
    #             self.assertEqual(SearchResult.PURE_PREFIX, trie.contains_prefix(list_data))

    def test_margin_cases(self):
        trie = DoubleArrayTrie(3)
        empty = []
        self.assertEqual(SearchResult.PURE_PREFIX, trie.contains_prefix(empty))

        not_in = [1, 2]
        self.assertEqual(SearchResult.NOT_FOUND, trie.contains_prefix(not_in))
        self.assertEqual(SearchResult.PURE_PREFIX, trie.contains_prefix(empty))

        one_in = [2]
        trie.add_to_trie(empty)
        trie.add_to_trie(one_in)
        trie.add_to_trie(empty)

        self.assertEqual(SearchResult.PURE_PREFIX, trie.contains_prefix(empty))
        self.assertEqual(SearchResult.PERFECT_MATCH, trie.contains_prefix(one_in))
        self.assertEqual(SearchResult.PURE_PREFIX, trie.contains_prefix(empty))

        one_in.append(1)
        self.assertEqual(SearchResult.NOT_FOUND, trie.contains_prefix(one_in))

    def test_counting_trie(self):
        trie = CountingTrie(4)
        string1 = [0, 1, 2, 3]
        string2 = [1, 2, 3]
        trie.add_to_trie(string1)
        trie.add_to_trie(string2)

        self.assertEqual(SearchResult.PERFECT_MATCH, trie.contains_prefix(string1))
        self.assertEqual(SearchResult.PERFECT_MATCH, trie.contains_prefix(string2))

        self.assertEqual(2, trie.get_search_count_for(string1))
        self.assertEqual(3, trie.get_search_count_for(string1))
        self.assertEqual(2, trie.get_search_count_for(string2))
        self.assertEqual(3, trie.get_search_count_for(string2))
        string3 = [1, 2]
        self.assertEqual(0, trie.get_search_count_for(string3))

if __name__ == "__main__":
    unittest.main()

"""
"""

from unittest import TestCase

from sort import SortContext, BubbleSortStrategy, InsertionSortStrategy, MergeSortStrategy


class SortTestCase(TestCase):
    """"""

    def test_should_sort_using_bubble_sort_strategy(self):
        """"""
        data = [5, 2, 8, 1, 9]

        bubble_sort_strategy = BubbleSortStrategy()
        context = SortContext(bubble_sort_strategy)

        context.sort_data(data)
        
        actual = data
        expected = [1, 2, 5, 8, 9]

        self.assertListEqual(actual, expected)

    def test_should_raise_exception_when_sorting_empty_list_using_bubble_sort_strategy(self):
        """"""
        data = []

        bubble_sort_strategy = BubbleSortStrategy()
        context = SortContext(bubble_sort_strategy)

        with self.assertRaises(ValueError):
            context.sort_data(data)

    def test_should_sort_using_insertion_sort_strategy(self):
        """"""
        data = [5, 2, 8, 1, 9]

        insertion_sort_strategy = InsertionSortStrategy() 
        context = SortContext(insertion_sort_strategy)

        context.sort_data(data)
        
        actual = data
        expected = [1, 2, 5, 8, 9]

        self.assertListEqual(actual, expected)

    def test_should_raise_exception_when_sorting_empty_list_using_insertion_sort_strategy(self):
        """"""
        data = []

        insertion_sort_strategy = InsertionSortStrategy()
        context = SortContext(insertion_sort_strategy)

        with self.assertRaises(ValueError):
            context.sort_data(data)

    def test_should_sort_using_merge_sort_strategy(self):
        """"""
        data = [5, 2, 8, 1, 9]

        merge_sort_strategy = MergeSortStrategy()
        context = SortContext(merge_sort_strategy)

        context.sort_data(data)
        
        actual = data
        expected = [1, 2, 5, 8, 9]

        self.assertListEqual(actual, expected)

    def test_should_raise_exception_when_sorting_empty_list_using_merge_sort_strategy(self):
        """"""
        data = []

        merge_sort_strategy = MergeSortStrategy()
        context = SortContext(merge_sort_strategy)

        with self.assertRaises(ValueError):
            context.sort_data(data)

"""
"""

from typing import List
from abc import ABC, abstractmethod


class SortStrategy(ABC):
    """
    """

    @abstractmethod
    def sort(self, data: List[int]):
        """"""


class BubbleSortStrategy(SortStrategy):
    """"""

    def sort(self, data: List[int]):
        """"""
        if not data:
            raise ValueError("data cannot be empty")

        n = len(data)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]


class InsertionSortStrategy(SortStrategy):
    """"""

    def sort(self, data: List[int]):
        """"""
        if not data:
            raise ValueError("data cannot be empty")

        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key


class MergeSortStrategy(SortStrategy):
    """"""

    def sort(self, data: List[int]):
        """"""
        if not data:
            raise ValueError("data cannot be empty")

        if len(data) <= 1:
            return

        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        self.sort(left_half)
        self.sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1


class SortContext:
    """"""
    _strategy: SortStrategy

    def __init__(self, strategy: SortStrategy):
        """"""
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data: List[int]):
        self._strategy.sort(data)


def main():
    """"""
    data_1 = [5, 2, 8, 1, 9]

    print("Bubble Sort")
    print(data_1)

    context = SortContext(BubbleSortStrategy())
    context.sort_data(data_1)

    print(data_1)

    data_2 = [5, 2, 8, 1, 9]

    print("Insertion Sort")
    print(data_2)

    context.set_strategy(InsertionSortStrategy())
    context.sort_data(data_2)

    print(data_2)

    data_3 = [5, 2, 8, 1, 9]

    print("Merge Sort")
    print(data_3)

    context.set_strategy(MergeSortStrategy())
    context.sort_data(data_3)

    print(data_3)


if __name__ == "__main__":
    main()

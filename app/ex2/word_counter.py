"""
"""

from typing import List
from abc import ABC, abstractmethod


class Observer(ABC):
    """"""

    @abstractmethod
    def update(self, word: str) -> int:
        """"""


class CountWordsObserver(Observer):
    """"""

    def update(self, word: str) -> int:
        """"""
        count = len(word.split())
        print(f"Total de palavras: {count}")

        return count


class CountEvenLengthWordsObserver(Observer):
    """"""

    def update(self, word: str) -> int:
        """"""
        words = word.split()
        even_length_words = [word for word in words if len(word) % 2 == 0]
        count = len(even_length_words)
        print(f"Total de palavras com quantidade par de caracteres: {count}")

        return count


class CountCapitalizedWordsObserver(Observer):
    """"""

    def update(self, word: str) -> int:
        """"""
        words = word.split()
        capitalized_words = [word for word in words if word[0].isupper()]
        count = len(capitalized_words)
        print(f"Total de palavras começadas com maiúsculas: {count}")

        return count


class WordCounter:
    """"""
    _observers: List[Observer]

    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def receive_sentence(self, sentence: str):
        for observer in self._observers:
            observer.update(sentence)


def main():
    """"""
    sentence = input("Digite uma frase: ")

    word_counter = WordCounter()
    word_counter.add_observer(CountWordsObserver())
    word_counter.add_observer(CountEvenLengthWordsObserver())
    word_counter.add_observer(CountCapitalizedWordsObserver())

    word_counter.receive_sentence(sentence)


if __name__ == "__main__":
    main()

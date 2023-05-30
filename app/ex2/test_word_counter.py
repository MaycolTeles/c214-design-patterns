"""
"""

from unittest import TestCase

from word_counter import WordCounter, CountWordsObserver, CountEvenLengthWordsObserver, CountCapitalizedWordsObserver


class WordCounterTestCase(TestCase):
    """"""

    def setUp(self):
        """"""
        self._word_counter = WordCounter()

    def test_count_words_observer(self):
        """"""
        test_sentence = "This is a test sentence."
        observer = CountWordsObserver()

        actual = observer.update(test_sentence)
        expected = 5

        self.assertEqual(actual, expected)

    def test_count_even_length_words_observer(self):
        """"""
        test_sentence = "This sentence has words with even lengths."
        observer = CountEvenLengthWordsObserver()

        actual = observer.update(test_sentence)
        expected = 5

        self.assertEqual(actual, expected)

    def test_count_capitalized_words_observer(self):
        """"""
        test_sentence = "Many Capitalized Words in this Sentence."
        observer = CountCapitalizedWordsObserver()
        
        actual = observer.update(test_sentence)
        expected = 4

        self.assertEqual(actual, expected)

    def test_empty_sentence(self):
        """"""
        test_sentence = ""
        observer = CountWordsObserver()

        actual = observer.update(test_sentence)
        expected = 0

        self.assertEqual(actual, expected)

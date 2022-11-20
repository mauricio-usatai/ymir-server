from .find_largest_number import FindLargestNumber
from .find_smallest_number import FindSmallestNumber
from .find_smallest_positive_number import FindSmallestPositiveNumber
from .is_palindrome import IsPalindrome
from .numeric_list_reverse import NumericListReverse
from .sort_numeric_list_asc_bubble import SortNumericListAscBubble
from .sort_numeric_list_asc_selection import SortNumericListAscSelection
from .string_reverse import StringReverse
from .k_means_classifier import KMeansClassifier
from .number_ner import NumberNER
from .remove_stopwords import RemoveStopWords
from .multiply_list_by_3 import MultiplyListBy3
from .odd_numbers_list import OddNumbersList
from .count_words import CountWords
from .is_subset import IsSubset
from .dataset_row_append import DataSetRowAppend
from .parse_json import ParseJson

class SolutionFactory():
    def create(self, solution):
        solution = eval(solution)
        return solution()
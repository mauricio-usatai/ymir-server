from .solution import Solution

class FindSmallestPositiveNumber(Solution):
    def apply(self, numbers):
        _min = float('inf')
        for n in numbers:
            if n < _min and n >= 0:
                _min = n
        return _min
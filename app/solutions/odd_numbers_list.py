from .solution import Solution

class OddNumbersList(Solution):
    def apply(self, _list):
        return [n for n in _list if n % 2 == 1]
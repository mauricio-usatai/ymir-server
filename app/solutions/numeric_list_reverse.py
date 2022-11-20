from .solution import Solution

class NumericListReverse(Solution):
    def apply(self, _list):
        _list = _list.copy()
        _list.reverse()
        return _list
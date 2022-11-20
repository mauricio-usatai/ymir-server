from .solution import Solution

class IsSubset(Solution):
    def apply(self, dicts):
        d1, d2 = dicts
        return d1.items() <= d2.items()
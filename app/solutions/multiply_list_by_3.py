from .solution import Solution

class MultiplyListBy3(Solution):
    def apply(self, numbers):
        return [n * 3 for n in numbers]
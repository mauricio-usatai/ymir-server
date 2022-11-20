from .solution import Solution

class IsPalindrome(Solution):
    def apply(self, string):
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True
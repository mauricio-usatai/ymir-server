from abc import ABC, abstractmethod

class Solution(ABC):
    @abstractmethod
    def apply(self, _input):
        raise NotImplementedError

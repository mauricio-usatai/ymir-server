import re

from .solution import Solution

class NumberNER(Solution):

    numbers = {
        'one': 1,
        'two': 2,
        'three': 3
    }

    def clean(self, s):
        print(s)
        s = re.sub(r'[,.]', ' ', s)
        s = re.sub(r'\s+', ' ', s)
        return s

    def apply(self, utterance):
        utterance = self.clean(utterance)

        entity_values = []        
        for token in utterance.split(' '):
            if token in self.numbers:
                entity_values.append(numbers[token])
        return entity_values
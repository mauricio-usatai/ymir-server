import re
from .solution import Solution

class CountWords(Solution):
    def clean(self, text):
        cleaned = re.sub(r'[!?\.,-]+', ' ', text.lower())
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned

    def apply(self, text):
        words_count = {}

        text = self.clean(text)
        for token in text.split():
            if token not in words_count:
                words_count[token] = 0

            words_count[token] += 1

        sorted_words_count = {word:words_count[word] for word in sorted(words_count)}
        return sorted_words_count
    
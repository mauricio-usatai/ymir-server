import re

from .solution import Solution

class RemoveStopWords(Solution):

    stop_words = ['the', 'and']

    def clean(self, s):
        s = re.sub(r'[\.!?,]', ' ', s)
        s = re.sub(r'\s+', ' ', s)
        return s

    def apply(self, utterance):
        utterance = self.clean(utterance)
        utterance = utterance.lower()

        for stop_word in self.stop_words:
            utterance = re.sub(r'^|[\s]?' + stop_word + r'(?![a-z])', ' ', utterance)

        utterance = re.sub(r'\s+', ' ', utterance)
        utterance = utterance.strip()
        return utterance

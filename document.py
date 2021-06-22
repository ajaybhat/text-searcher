from collections import Counter


class Document:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.timestamp = -1
        self.word_count = self.generate_word_count(text)

    def generate_word_count(self, text):
        word_count = {}
        if text is not None:
            word_count = dict(Counter(text.split()))
        return word_count

    def __str__(self):
        return f'Document #{self.timestamp}: {self.name} - {self.text}'

    def __repr__(self):
        return self.__str__()
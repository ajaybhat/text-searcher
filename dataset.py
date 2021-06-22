from order import Order

ID = 0


class Dataset:
    def __init__(self, name, documents=[]):
        self.name = name
        self.documents = []
        for document in documents:
            self.insert(document)
        self.default_order = Order.SEARCH_TERM

    def insert(self, document):
        global ID

        ID += 1
        document.timestamp = ID
        self.documents.append(document)
        self.reverse_index = self.generate_reverse_index()

    def delete(self, document):
        self.documents = list(filter(lambda doc: doc.name != document.name, self.documents))
        self.reverse_index = self.generate_reverse_index()

    def generate_reverse_index(self):
        reverse_index = {}
        for document in self.documents:
            for word in document.word_count:
                documents = reverse_index.get(word, [])
                # Check if doc is already in reverse index for this word
                filtered_docs = list(filter(lambda doc: doc.name == document.name, documents))
                if len(filtered_docs) > 0:
                    pass
                else:
                    documents.append(document)
                    reverse_index[word] = documents
        return reverse_index

    def __str__(self):
        return f'Dataset: {self.name}\n {self.documents}\n Order: {self.default_order}'

    def __repr__(self):
        return self.__str__()

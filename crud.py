from dataset import Dataset
from document import Document


def create_dataset(name, documents=[]):
    return Dataset(name, documents)


def create_document(name, text):
    return Document(name, text)

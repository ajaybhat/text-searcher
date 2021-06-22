from crud import create_document, create_dataset
from document import Document
from order import Order
from search import search

if __name__ == '__main__':
    document = create_document('Doc1', 'apple is a fruit')
    dataset = create_dataset('Dataset A', [document])
    dataset.insert(Document('Doc2', 'apple apple come on.'))
    dataset.insert(Document('Doc3', 'oranges are sour'))
    dataset.insert(Document('Doc4', 'apple is sweet'))
    print(dataset)

    #print(search(dataset, ["apple"], Order.SEARCH_TERM))
    #print(search(None, ["apple"], Order.SEARCH_TERM))
    print(search(dataset, ["apple", "is"], Order.SEARCH_TERM))

    #print(search(dataset, ["apple"], Order.RECENCY))
    #print(search(dataset, ["apple"], descending=False))



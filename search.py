from order import Order
from search_helper import search_dataset, order_results


def search(dataset, search_terms, order=Order.SEARCH_TERM, descending=True):
    search_results = search_dataset(search_terms, dataset)
    ordered_results = order_results(dataset, search_results, search_terms, order_override=order,
                                    descending=descending)
    return ordered_results

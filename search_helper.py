from order import Order


def search_dataset(search_terms, dataset):
    search_result = None
    for term in search_terms:
        interim_result = dataset.reverse_index.get(term, [])
        if search_result is None:
            search_result = interim_result
        else:
            search_result = [result for result in search_result if result in interim_result]
    return search_result


def sort_by_recency(search_results, descending=True):
    return sorted(search_results, key=lambda doc: doc.timestamp, reverse=descending)


def sort_by_search_terms_occurence(search_results, search_terms, descending=True):
    return sorted(search_results, key=lambda doc: sum([doc.word_count[term] for term in search_terms]),
                  reverse=descending)


def order_results(dataset, search_results, search_terms, order_override=None, descending=True):
    ordered_results = []
    order = dataset.default_order
    if order_override:
        order = order_override
    if order == Order.SEARCH_TERM:
        ordered_results = sort_by_search_terms_occurence(search_results, search_terms, descending=descending)
    elif order == Order.RECENCY:
        ordered_results = sort_by_recency(search_results, descending=descending)
    return ordered_results

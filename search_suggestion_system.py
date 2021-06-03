def suggestedProducts(products, searchWord):
    from collections import defaultdict
    product_catalog = defaultdict(list)
    for product in products:
        for i in range(1, len(product) + 1):
            _key = product[:i]
            product_catalog[_key].append(product)
    #print(product_catalog)
    result = []
    for i in range(1, len(searchWord) + 1):
        _key = searchWord[:i]
        result.append(sorted(product_catalog[_key])[:3])
    return result


products =  ["bags","baggage","banner","box","cloths"]
searchWord = 'bags'
result = suggestedProducts(products, searchWord)
print(result)

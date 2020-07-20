def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(length):
        v = weights[i]
        if limit-v in cache:
            if limit-v > v:
                return [cache[limit-v], i]
            else:
                return [i, cache[limit-v]]
        cache[v] = i
    return None

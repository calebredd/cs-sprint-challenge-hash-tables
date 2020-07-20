def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for a in arrays[0]:
        if a not in cache:
            cache[a] = 1
    for i in range(1, len(arrays)):
        for a in arrays[i]:
            if a in cache:
                cache[a] = cache[a] + 1

    result = []
    for c in cache:
        if cache[c] == len(arrays):
            result.append(c)
    return result


if __name__ == "__main__":
    arrays = []
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
